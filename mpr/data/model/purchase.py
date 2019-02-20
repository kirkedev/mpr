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


class Purchase(NamedTuple):
    date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32

    @property
    def purchase_type(self):
        return PurchaseType(
            seller=Seller.from_ordinal(self.seller),
            arrangements=Arrangement.from_ordinal(self.arrangement),
            basis=Basis.from_ordinal(self.basis))


dtype = np.dtype(list(Purchase._field_types.items()))


def to_array(records: Iterator[Purchase]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
