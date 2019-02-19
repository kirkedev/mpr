from enum import Enum
from typing import NamedTuple
from typing import Iterator
from datetime import date
from datetime import datetime
from functools import singledispatch

from numpy import datetime64
from numpy import float32

from . import Report
from . import Attributes
from . import date_interval
from . import fetch
from . import filter_sections

date_format = "%m/%d/%Y"


class Section(Enum):
    CUTOUT = 'Cutout and Primal Values'
    # DAILY_CHANGE = 'Change From Prior Day'
    # FIVE_DAY_AVERAGE = '5-Day Average Cutout and Primal Values'
    VOLUME = 'Current Volume'
    # LOIN = 'Loin Cuts'
    # BUTT = 'Butt Cuts'
    # PICNIC = 'Picnic Cuts'
    # HAM = 'Ham Cuts'
    # BELLY = 'Belly Cuts'
    # RIB = 'Sparerib Cuts'
    # JOWL = 'Jowl Cuts'
    # TRIM = 'Trim Cuts'
    # VARIETY = 'Variety Cuts'
    # ADDED_INGREDIENT = 'Added Ingredient Cuts'


class Record(NamedTuple):
    date: datetime64
    primal_loads: float32
    trimming_loads: float32
    carcass_price: float32
    loin_price: float32
    butt_price: float32
    picnic_price: float32
    rib_price: float32
    ham_price: float32
    belly_price: float32


def parse_attributes(sections: Iterator[Attributes]) -> Record:
    volume, cutout = sections
    report_date = datetime.strptime(volume['report_date'], date_format).date()

    return Record(
        date=datetime64(report_date),
        primal_loads=float32(volume['temp_cuts_total_load']),
        trimming_loads=float32(volume['temp_process_total_load']),
        carcass_price=float32(cutout['pork_carcass']),
        loin_price=float32(cutout['pork_loin']),
        butt_price=float32(cutout['pork_butt']),
        picnic_price=float32(cutout['pork_picnic']),
        rib_price=float32(cutout['pork_rib']),
        ham_price=float32(cutout['pork_ham']),
        belly_price=float32(cutout['pork_belly']))


async def fetch_cutout(report: Report, start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(report, start_date, end_date)
    return map(parse_attributes, filter_sections(response, Section.VOLUME.value, Section.CUTOUT.value))


@singledispatch
async def morning(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_cutout(Report.CUTOUT_MORNING, start_date, end_date)


@singledispatch
async def afternoon(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_cutout(Report.CUTOUT_AFTERNOON, start_date, end_date)


@morning.register(int)
async def morning_days(days: int) -> Iterator[Record]:
    return await morning(*date_interval(days))


@afternoon.register(int)
async def afternoon_days(days: int) -> Iterator[Record]:
    return await afternoon(*date_interval(days))


lm_pk602 = pk602 = morning
lm_pk603 = pk603 = afternoon
