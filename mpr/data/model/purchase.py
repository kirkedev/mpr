from abc import ABC
from datetime import date

from numpy import datetime64

from tables import Time32Col
from tables import UInt32Col
from tables import Float32Col
from tables.tableextension import Row

from mpr.data.api.purchase import Record

from .observation import Observation
from .purchase_type import PurchaseType
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis
from .purchase_type import PurchaseTypeCol


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
