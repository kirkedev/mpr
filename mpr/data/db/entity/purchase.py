from abc import ABC
from datetime import date

from numpy import dtype
from numpy import uint32
from numpy import float32
from numpy import datetime64
from tables.tableextension import Row

from mpr.data.model.purchase import Purchase
from mpr.data.model.purchase_type import purchase_type
from .observation import Observation


class PurchaseEntity(Observation[Purchase], ABC):
    schema = dtype([
        ('date', uint32),
        ('purchase_type', purchase_type),
        ('head_count', uint32),
        ('avg_price', float32),
        ('low_price', float32),
        ('high_price', float32)
    ])

    @classmethod
    def from_row(cls, row: Row) -> Purchase:
        return Purchase(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            purchase_type=row['purchase_type'],
            head_count=row['head_count'],
            avg_price=row['avg_price'],
            low_price=row['low_price'],
            high_price=row['high_price'])

    @classmethod
    def append(cls, record: Purchase):
        row = cls.table.row

        row['date'] = record.date.astype(date).toordinal()
        row['purchase_type'] = record.purchase_type
        row['head_count'] = record.head_count
        row['avg_price'] = record.avg_price
        row['low_price'] = record.low_price
        row['high_price'] = record.high_price

        row.append()

    @staticmethod
    def to_row(record: Purchase):
        return (
            record.date.astype(date).toordinal(),
            record.purchase_type,
            record.head_count,
            record.avg_price,
            record.low_price,
            record.high_price)
