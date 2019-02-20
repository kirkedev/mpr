from typing import NamedTuple
from typing import Iterator
from datetime import datetime

import numpy as np
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import datetime64
from numpy import recarray

from . import Attributes
from . import Date
from . import opt_int
from . import opt_float

from .purchase_type import PurchaseType
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis
from .purchase_type import purchase_types

date_format = "%m/%d/%Y"


class Slaughter(NamedTuple):
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

    @property
    def purchase_type(self):
        return PurchaseType(
            seller=Seller.from_ordinal(self.seller),
            arrangements=Arrangement.from_ordinal(self.arrangement),
            basis=Basis.from_ordinal(self.basis))

    @property
    def total_weight(self) -> float:
        return self.head_count * self.carcass_weight if self.carcass_weight else 0.0

    @property
    def total_value(self) -> float:
        return self.total_weight * self.net_price if self.net_price else 0.0

    @classmethod
    def from_attributes(cls, attr: Attributes) -> 'Slaughter':
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


dtype = np.dtype(list(Slaughter._field_types.items()))


def to_array(records: Iterator[Slaughter]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
