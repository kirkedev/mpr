from typing import NamedTuple
from typing import Iterator

import numpy as np
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray

from . import Date

from .purchase_type import PurchaseType
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis


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


dtype = np.dtype(list(Slaughter._field_types.items()))


def to_array(records: Iterator[Slaughter]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
