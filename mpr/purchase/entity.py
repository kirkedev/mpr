from abc import ABC
from typing import Tuple

from numpy import dtype
from numpy import uint8
from numpy import uint32
from numpy import float32

from ..date import from_ordinal
from ..date import to_ordinal
from ..entity import Entity

from .model import Purchase


class PurchaseEntity(Entity[Purchase], ABC):
    schema = dtype([
        ('date', uint32),
        ('report_date', uint32),
        ('seller', uint8),
        ('arrangement', uint8),
        ('basis', uint8),
        ('head_count', uint32),
        ('avg_price', float32),
        ('low_price', float32),
        ('high_price', float32)
    ])

    @staticmethod
    def from_row(row: Tuple) -> Purchase:
        return Purchase(*map(from_ordinal, row[:2]), *row[2:])

    @staticmethod
    def to_row(record: Purchase) -> Tuple:
        return (*map(to_ordinal, record[:2]), *record[2:])
