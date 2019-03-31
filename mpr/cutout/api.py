from enum import Enum
from typing import Iterator
from datetime import date

from numpy import float32

from ..api import Attributes
from ..api import Report
from ..api import fetch
from ..api import filter_sections
from ..date import from_string

from .model import Cutout

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


def parse_attributes(cutout: Attributes, volume: Attributes) -> Cutout:
    report_date = from_string(cutout['report_date'], date_format)

    return Cutout(
        date=report_date,
        report_date=report_date,
        primal_loads=float32(volume['temp_cuts_total_load']),
        trimming_loads=float32(volume['temp_process_total_load']),
        carcass_price=float32(cutout['pork_carcass']),
        loin_price=float32(cutout['pork_loin']),
        butt_price=float32(cutout['pork_butt']),
        picnic_price=float32(cutout['pork_picnic']),
        rib_price=float32(cutout['pork_rib']),
        ham_price=float32(cutout['pork_ham']),
        belly_price=float32(cutout['pork_belly']))


async def fetch_cutout(report: Report, start: date, end=date.today()) -> Iterator[Cutout]:
    response = await fetch(report, start, end)

    return map(lambda it: parse_attributes(*it),
        filter_sections(response, Section.CUTOUT.value, Section.VOLUME.value))


async def morning(start: date, end=date.today()) -> Iterator[Cutout]:
    return await fetch_cutout(Report.CUTOUT_MORNING, start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Cutout]:
    return await fetch_cutout(Report.CUTOUT_AFTERNOON, start, end)


lm_pk600 = pk600 = morning
lm_pk602 = pk602 = afternoon
