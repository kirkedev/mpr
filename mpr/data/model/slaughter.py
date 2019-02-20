from abc import ABC
from typing import NamedTuple
from typing import Iterator
from datetime import datetime

import numpy as np
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import datetime64
from numpy import recarray

from tables import UInt32Col
from tables import Float32Col
from tables import Time32Col
from tables.tableextension import Row

from . import Attributes
from . import Date
from . import opt_int
from . import opt_float

from .observation import Observation
from .purchase_type import PurchaseType
from .purchase_type import PurchaseTypeCol
from .purchase_type import purchase_types

date_format = "%m/%d/%Y"


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

    @classmethod
    def from_attributes(cls, attr: Attributes) -> 'Record':
        report_date = datetime.strptime(attr['for_date_begin'], date_format).date()

        purchase_type = attr['purchase_type']
        (seller, arrangement, basis) = purchase_types[purchase_type]

        return cls(
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


dtype = np.dtype(list(Record._field_types.items()))


def to_array(records: Iterator[Record]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)


class Slaughter(Observation, ABC):
    date: datetime64
    seller: uint8
    arrangement: uint8
    basis: uint8
    purchase_type: PurchaseType
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

    schema = {
        'date': Time32Col(),
        'purchase_type': PurchaseTypeCol(),
        'head_count': UInt32Col(),
        'base_price': Float32Col(),
        'net_price': Float32Col(),
        'low_price': Float32Col(),
        'high_price': Float32Col(),
        'live_weight': Float32Col(),
        'carcass_weight': Float32Col(),
        'sort_loss': Float32Col(),
        'backfat': Float32Col(),
        'loin_depth': Float32Col(),
        'loineye_area': Float32Col(),
        'lean_percent': Float32Col()
    }

    @property
    def total_weight(self) -> float:
        return self.head_count * self.carcass_weight if self.carcass_weight else 0.0

    @property
    def total_value(self) -> float:
        return self.total_weight * self.net_price if self.net_price else 0.0

    def append(self):
        row = self.table.row

        row['date'] = self.date
        row['purchase_type/seller'] = self.seller
        row['purchase_type/arrangement'] = self.arrangement
        row['purchase_type/basis'] = self.basis
        row['head_count'] = self.head_count
        row['base_price'] = self.base_price
        row['net_price'] = self.net_price
        row['low_price'] = self.low_price
        row['high_price'] = self.high_price
        row['live_weight'] = self.live_weight
        row['carcass_weight'] = self.carcass_weight
        row['sort_loss'] = self.sort_loss
        row['backfat'] = self.backfat
        row['loin_depth'] = self.loin_depth
        row['loineye_area'] = self.loineye_area
        row['lean_percent'] = self.lean_percent

        row.append()

    @classmethod
    def from_row(cls, row: Row) -> 'Slaughter':
        return cls(row.fetch_all_fields())
