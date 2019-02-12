from datetime import date, datetime
from enum import Enum
from functools import singledispatch
from typing import Iterator, NamedTuple, Tuple

from . import Attributes, Report, fetch, filter_sections, opt_float, opt_int, date_format, date_interval

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
    date: date
    primal_loads: float
    trimming_loads: float
    carcass_price: float
    loin_price: float
    butt_price: float
    picnic_price: float
    rib_price: float
    ham_price: float
    belly_price: float

def parse_attributes(pair: Tuple[Attributes, Attributes]) -> Record:
    (cutout, volume) = pair

    return Record(
        date = datetime.strptime(volume['report_date'], date_format).date(),
        primal_loads = float(volume['temp_cuts_total_load']),
        trimming_loads = float(volume['temp_process_total_load']),
        carcass_price = float(cutout['pork_carcass']),
        loin_price = float(cutout['pork_loin']),
        butt_price = float(cutout['pork_butt']),
        picnic_price = float(cutout['pork_picnic']),
        rib_price = float(cutout['pork_rib']),
        ham_price = float(cutout['pork_ham']),
        belly_price = float(cutout['pork_belly']))

async def fetch_cutout(report: Report, start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(Report.PURCHASED_SWINE, start_date, end_date)
    return map(parse_attributes, filter_sections(response, Section.VOLUME.value, Section.CUTOUT.value))

@singledispatch
async def get_morning(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_cutout(Report.CUTOUT_MORNING, start_date, end_date)

@get_morning.register(int)
async def get_morning_days(days: int) -> Iterator[Record]:
    return await get_morning(*date_interval(days))

@singledispatch
async def get_afternoon(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_cutout(Report.CUTOUT_MORNING, start_date, end_date)

@get_afternoon.register(int)
async def get_afternoon_days(days: int) -> Iterator[Record]:
    return await get_afternoon(*date_interval(days))

lm_pk602 = pk602 = get_morning
lm_pk603 = pk603 = get_afternoon

if __name__ == "__main__":
    import pandas as pd
    data = pd.DataFrame.from_records(lm_pk603(10), columns=Record._fields, index='date')
    print(data)
