from abc import ABC
from typing import NamedTuple
from typing import Iterator
from datetime import date
from datetime import datetime

import numpy as np
from numpy import datetime64
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray

from tables import Time32Col
from tables import UInt32Col
from tables import Float32Col
from tables.tableextension import Row

from . import Attributes
from . import Date
from . import opt_float
from . import opt_int

from .observation import Observation
from .purchase_type import purchase_types
from .purchase_type import PurchaseTypeCol
from .purchase_type import PurchaseType
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis

date_format = "%m/%d/%Y"


class Record(NamedTuple):
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
    def from_attributes(cls, attr: Attributes) -> 'Record':
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


dtype = np.dtype(list(Record._field_types.items()))


def to_array(records: Iterator[Record]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)


class Purchase(Record, Observation, ABC):
    schema = {
        'date': Time32Col(),
        'purchase_type': PurchaseTypeCol(),
        'head_count': UInt32Col(),
        'avg_price': Float32Col(),
        'low_price': Float32Col(),
        'high_price': Float32Col()
    }

    @classmethod
    def from_row(cls, row: Row) -> 'Purchase':
        return cls(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            seller=row['purchase_type/seller'],
            arrangement=row['purchase_type/arrangement'],
            basis=row['purchase_type/basis'],
            head_count=row['head_count'],
            avg_price=row['avg_price'],
            low_price=row['low_price'],
            high_price=row['high_price'])

    def append(self):
        row = self.table.row

        row['date'] = self.date.astype(date).toordinal()
        row['purchase_type/seller'] = self.seller
        row['purchase_type/arrangement'] = self.arrangement
        row['purchase_type/basis'] = self.basis
        row['head_count'] = self.head_count
        row['avg_price'] = self.avg_price
        row['low_price'] = self.low_price
        row['high_price'] = self.high_price

        row.append()
