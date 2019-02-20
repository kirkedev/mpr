from typing import NamedTuple
from typing import Iterator

import numpy as np
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
    purchase_type: PurchaseType
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32

    @property
    def seller(self) -> Seller:
        return Seller.from_ordinal(self.purchase_type[0])

    @property
    def arrangement(self) -> Arrangement:
        return Arrangement.from_ordinal(self.purchase_type[1])

    @property
    def basis(self) -> Basis:
        return Basis.from_ordinal(self.purchase_type[2])


dtype = np.dtype(list(Purchase._field_types.items()))


def to_array(records: Iterator[Purchase]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
