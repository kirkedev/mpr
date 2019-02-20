from abc import ABC
from datetime import date

from numpy import datetime64
from tables import Time32Col
from tables import UInt32Col
from tables import Float32Col
from tables.tableextension import Row

from mpr.data.model.purchase import Purchase
from .observation import Observation
from .purchase_type import PurchaseTypeCol


class PurchaseEntity(Observation[Purchase], ABC):
    schema = {
        'date': Time32Col(),
        'purchase_type': PurchaseTypeCol(),
        'head_count': UInt32Col(),
        'avg_price': Float32Col(),
        'low_price': Float32Col(),
        'high_price': Float32Col()
    }

    @classmethod
    def from_row(cls, row: Row) -> Purchase:
        return Purchase(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            seller=row['purchase_type/seller'],
            arrangement=row['purchase_type/arrangement'],
            basis=row['purchase_type/basis'],
            head_count=row['head_count'],
            avg_price=row['avg_price'],
            low_price=row['low_price'],
            high_price=row['high_price'])

    @classmethod
    def append(cls, record: Purchase):
        row = cls.table.row

        row['date'] = record.date.astype(date).toordinal()
        row['purchase_type/seller'] = record.seller
        row['purchase_type/arrangement'] = record.arrangement
        row['purchase_type/basis'] = record.basis
        row['head_count'] = record.head_count
        row['avg_price'] = record.avg_price
        row['low_price'] = record.low_price
        row['high_price'] = record.high_price

        row.append()
