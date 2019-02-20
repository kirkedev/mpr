from enum import Enum
from typing import Iterator
from datetime import date
from datetime import timedelta
from functools import singledispatch

from mpr.data.model.slaughter import Record

from . import Report
from . import date_interval
from . import fetch
from . import filter_section


class Section(Enum):
    # SUMMARY = 'Summary'
    BARROWS_AND_GILTS = 'Barrows/Gilts'
    # CARCASS_MEASUREMENTS = 'Carcass Measurements'
    # SOWS_AND_BOARS = 'Sows/Boars'
    # SCHEDULED_SWINE = '14-Day Scheduled Swine'
    # NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'


@singledispatch
async def fetch_slaughter(start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(Report.SLAUGHTERED_SWINE, start_date + timedelta(days=1), end_date)
    return map(Record.from_attributes, filter_section(response, Section.BARROWS_AND_GILTS.value))


@fetch_slaughter.register(int)
async def fetch_slaughter_days(days: int) -> Iterator[Record]:
    return await fetch_slaughter(*date_interval(days))


lm_hg201 = hg201 = fetch_slaughter
