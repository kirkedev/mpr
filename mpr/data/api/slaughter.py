from enum import Enum
from typing import NamedTuple
from typing import Iterator
from datetime import date
from datetime import datetime
from datetime import timedelta
from functools import singledispatch

import numpy as np
from numpy import datetime64
from numpy import uint8
from numpy import uint32
from numpy import float32

from mpr.data.model.purchase_type import purchase_types

from . import Report
from . import Attributes
from . import Date
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
    date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    base_price: float32
    net_price: float32
    low_price: float32
    high_price: float32
    live_weight: float32
    carcass_weight: float32
    sort_loss: float32
    backfat: float32
    loin_depth: float32
    loineye_area: float32
    lean_percent: float32


dtype = np.dtype(list(Record._field_types.items()))


def parse_attributes(attr: Attributes) -> Record:
    report_date = datetime.strptime(attr['for_date_begin'], date_format).date()

    purchase_type = attr['purchase_type']
    (seller, arrangement, basis) = purchase_types[purchase_type]

    return Record(
        date=datetime64(report_date, 'D'),
        seller=seller.to_ordinal(),
        arrangement=arrangement.to_ordinal(),
        basis=basis.to_ordinal(),
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
async def fetch_slaughter(start_date: date, end_date=date.today()) -> Iterator[Record]:
    response = await fetch(Report.SLAUGHTERED_SWINE, start_date + timedelta(days=1), end_date)
    return map(parse_attributes, filter_section(response, Section.BARROWS_AND_GILTS.value))


@fetch_slaughter.register(int)
async def fetch_slaughter_days(days: int) -> Iterator[Record]:
    return await fetch_slaughter(*date_interval(days))


lm_hg201 = hg201 = fetch_slaughter
