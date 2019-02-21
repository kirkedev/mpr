from typing import NamedTuple
from typing import Iterator

import numpy as np
from numpy import uint32
from numpy import float32
from numpy import recarray

from . import date_type
from . import Date
from .purchase_type import purchase_type
from .purchase_type import PurchaseType
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis


class Purchase(NamedTuple):
    date: Date
    purchase_type: PurchaseType
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32

    @property
    def seller(self) -> Seller:
        seller = self.purchase_type[0]
        return Seller(seller)

    @property
    def arrangement(self) -> Arrangement:
        arrangement = self.purchase_type[1]
        return Arrangement(arrangement)

    @property
    def basis(self) -> Basis:
        basis = self.purchase_type[2]
        return Basis(basis)


dtype = np.dtype([
    ('date', date_type),
    ('purchase_type', purchase_type),
    ('head_count', uint32),
    ('avg_price', float32),
    ('low_price', float32),
    ('high_price', float32)
])


def to_array(records: Iterator[Purchase]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
