from abc import ABC
from typing import Tuple
from datetime import date

from numpy import dtype
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import datetime64
from tables.tableextension import Row

from mpr.data.model.purchase import Purchase
from .observation import Observation


class PurchaseEntity(Observation[Purchase], ABC):
    schema = dtype([
        ('date', uint32),
        ('seller', uint8),
        ('arrangement', uint8),
        ('basis', uint8),
        ('head_count', uint32),
        ('avg_price', float32),
        ('low_price', float32),
        ('high_price', float32)
    ])

    @classmethod
    def from_row(cls, row: Row) -> Purchase:
        return Purchase(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            seller=row['seller'],
            arrangement=row['arrangement'],
            basis=row['basis'],
            head_count=row['head_count'],
            avg_price=row['avg_price'],
            low_price=row['low_price'],
            high_price=row['high_price'])

    @staticmethod
    def to_row(record: Purchase) -> Tuple:
        return (
            record.date.astype(date).toordinal(),
            record.seller,
            record.arrangement,
            record.basis,
            record.head_count,
            record.avg_price,
            record.low_price,
            record.high_price)
