from enum import Enum
from typing import NamedTuple
from typing import Optional
from typing import Iterator
from datetime import date
from datetime import datetime
from datetime import timedelta
from functools import singledispatch

from . import Report
from . import Attributes
from . import opt_float
from . import opt_int
from . import date_interval
from . import fetch
from . import filter_section

date_format = "%m/%d/%Y"


class Section(Enum):
    # VOLUME = 'Current Volume by Purchase Type'
    BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
    # CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
    # CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
    # AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
    # SOWS = 'Sows'
    # STATES = 'State of Origin'


class Record(NamedTuple):
    date: date
    purchase_type: str
    head_count: int
    avg_price: Optional[float]
    low_price: Optional[float]
    high_price: Optional[float]


def parse_attributes(attr: Attributes) -> Record:
    report_date = attr['reported_for_date']
    purchase_type = attr['purchase_type']

    return Record(
        date=datetime.strptime(report_date, date_format).date(),
        purchase_type=purchase_type,
        head_count=opt_int(attr, 'head_count') or 0,
        avg_price=opt_float(attr, 'wtd_avg'),
        low_price=opt_float(attr, 'price_low'),
        high_price=opt_float(attr, 'price_high'))


async def fetch_purchase(report: Report, start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(report, start_date, end_date)
    return map(parse_attributes, filter_section(response, Section.BARROWS_AND_GILTS.value))


@singledispatch
async def get_prior_day(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_purchase(Report.PURCHASED_SWINE, start_date + timedelta(days=1), end_date)


@singledispatch
async def get_morning(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_purchase(Report.DIRECT_HOG_MORNING, start_date, end_date)


@singledispatch
async def get_afternoon(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_purchase(Report.DIRECT_HOG_AFTERNOON, start_date, end_date)


@get_prior_day.register(int)
async def get_prior_days(days: int) -> Iterator[Record]:
    return await get_prior_day(*date_interval(days))


@get_morning.register(int)
async def get_morning_days(days: int) -> Iterator[Record]:
    return await get_morning(*date_interval(days))


@get_afternoon.register(int)
async def get_afternoon_days(days: int) -> Iterator[Record]:
    return await get_afternoon(*date_interval(days))


lm_hg200 = hg200 = get_prior_day
lm_hg202 = hg202 = get_morning
lm_hg203 = hg203 = get_afternoon
