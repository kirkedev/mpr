from enum import Enum
from typing import NamedTuple
from typing import Iterator
from datetime import date
from datetime import datetime
from datetime import timedelta
from functools import singledispatch

from numpy import datetime64
from numpy import uint8
from numpy import uint32
from numpy import float32

from mpr.data.model.purchase_type import purchase_types

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
    date: datetime64
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32


def parse_attributes(attr: Attributes) -> Record:
    report_date = datetime.strptime(attr['reported_for_date'], date_format).date()

    purchase_type = attr['purchase_type']
    (seller, arrangement, basis) = purchase_types[purchase_type]

    return Record(
        date=datetime64(report_date),
        seller=seller.to_ordinal(),
        arrangement=arrangement.to_ordinal(),
        basis=basis.to_ordinal(),
        head_count=opt_int(attr, 'head_count') or 0,
        avg_price=opt_float(attr, 'wtd_avg'),
        low_price=opt_float(attr, 'price_low'),
        high_price=opt_float(attr, 'price_high'))


async def fetch_purchase(report: Report, start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(report, start_date, end_date)
    return map(parse_attributes, filter_section(response, Section.BARROWS_AND_GILTS.value))


@singledispatch
async def prior_day(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_purchase(Report.PURCHASED_SWINE, start_date + timedelta(days=1), end_date)


@singledispatch
async def morning(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_purchase(Report.DIRECT_HOG_MORNING, start_date, end_date)


@singledispatch
async def afternoon(start_date: date, end_date=date.today()) -> Iterator[Record]:
    return await fetch_purchase(Report.DIRECT_HOG_AFTERNOON, start_date, end_date)


@prior_day.register(int)
async def prior_days(days: int) -> Iterator[Record]:
    return await prior_day(*date_interval(days))


@morning.register(int)
async def morning_days(days: int) -> Iterator[Record]:
    return await morning(*date_interval(days))


@afternoon.register(int)
async def afternoon_days(days: int) -> Iterator[Record]:
    return await afternoon(*date_interval(days))


lm_hg200 = hg200 = prior_day
lm_hg202 = hg202 = morning
lm_hg203 = hg203 = afternoon
