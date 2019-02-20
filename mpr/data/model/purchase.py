from typing import NamedTuple
from typing import Iterator
from datetime import datetime

import numpy as np
from numpy import datetime64
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray

from . import Attributes
from . import Date
from . import opt_float
from . import opt_int

from .purchase_type import purchase_types
from .purchase_type import PurchaseType
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis

date_format = "%m/%d/%Y"


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

    @classmethod
    def from_attributes(cls, attr: Attributes) -> 'Purchase':
        report_date = datetime.strptime(attr['reported_for_date'], date_format).date()

        purchase_type = attr['purchase_type']
        (seller, arrangement, basis) = purchase_types[purchase_type]

        return cls(
            date=datetime64(report_date, 'D'),
            seller=seller.to_ordinal(),
            arrangement=arrangement.to_ordinal(),
            basis=basis.to_ordinal(),
            head_count=opt_int(attr, 'head_count') or 0,
            avg_price=opt_float(attr, 'wtd_avg'),
            low_price=opt_float(attr, 'price_low'),
            high_price=opt_float(attr, 'price_high'))


dtype = np.dtype(list(Purchase._field_types.items()))


def to_array(records: Iterator[Purchase]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
