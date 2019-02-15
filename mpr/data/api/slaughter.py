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
    # SUMMARY = 'Summary'
    BARROWS_AND_GILTS = 'Barrows/Gilts'
    # CARCASS_MEASUREMENTS = 'Carcass Measurements'
    # SOWS_AND_BOARS = 'Sows/Boars'
    # SCHEDULED_SWINE = '14-Day Scheduled Swine'
    # NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'


class Record(NamedTuple):
    date: date
    purchase_type: str
    head_count: int
    base_price: Optional[float]
    net_price: Optional[float]
    low_price: Optional[float]
    high_price: Optional[float]
    live_weight: Optional[float]
    carcass_weight: Optional[float]
    sort_loss: Optional[float]
    backfat: Optional[float]
    loin_depth: Optional[float]
    loineye_area: Optional[float]
    lean_percent: Optional[float]


def parse_attributes(attr: Attributes) -> Record:
    report_date = attr['for_date_begin']
    purchase_type = attr['purchase_type']

    return Record(
        date=datetime.strptime(report_date, date_format).date(),
        purchase_type=purchase_type,
        head_count=opt_int(attr, 'head_count') or 0,
        base_price=opt_float(attr, 'base_price'),
        net_price=opt_float(attr, 'avg_net_price'),
        low_price=opt_float(attr, 'lowest_net_price'),
        high_price=opt_float(attr, 'highest_net_price'),
        live_weight=opt_float(attr, 'avg_live_weight'),
        carcass_weight=opt_float(attr, 'avg_carcass_weight'),
        sort_loss=opt_float(attr, 'avg_sort_loss'),
        backfat=opt_float(attr, 'avg_backfat'),
        loin_depth=opt_float(attr, 'avg_loin_depth'),
        loineye_area=opt_float(attr, 'loineye_area'),
        lean_percent=opt_float(attr, 'avg_lean_percent'))


@singledispatch
async def slaughter(start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(Report.SLAUGHTERED_SWINE, start_date + timedelta(days=1), end_date)
    return map(parse_attributes, filter_section(response, Section.BARROWS_AND_GILTS.value))


@slaughter.register(int)
async def slaughter_days(days: int) -> Iterator[Record]:
    return await slaughter(*date_interval(days))


lm_hg201 = hg201 = slaughter
