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

    @staticmethod
    def from_row(row: Row) -> Purchase:
        return Purchase(datetime64(date.fromordinal(row[0]), 'D'), *row[1:])

    @staticmethod
    def to_row(record: Purchase) -> Tuple:
        return (record[0].astype(date).toordinal(), *record[1:])
