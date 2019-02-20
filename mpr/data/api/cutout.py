from enum import Enum
from typing import Iterator
from datetime import date
from functools import singledispatch

from mpr.data.model.cutout import Record

from . import Report
from . import date_interval
from . import fetch
from . import filter_sections


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


async def fetch_cutout(report: Report, start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(report, start_date, end_date)
    return map(Record.from_attributes, *filter_sections(response, Section.VOLUME.value, Section.CUTOUT.value))


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
