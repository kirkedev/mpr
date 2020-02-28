from typing import Tuple

from numpy import dtype
from numpy import uint8
from numpy import uint32
from numpy import float32

from ..date import to_ordinal
from ..date import from_ordinal
from ..entity import Entity

from .model import Slaughter


class SlaughterEntity(Entity[Slaughter]):
    schema = dtype([
        ('date', uint32),
        ('report_date', uint32),
        ('seller', uint8),
        ('arrangement', uint8),
        ('basis', uint8),
        ('head_count', uint32),
        ('base_price', float32),
        ('net_price', float32),
        ('low_price', float32),
        ('high_price', float32),
        ('live_weight', float32),
        ('carcass_weight', float32),
        ('sort_loss', float32),
        ('backfat', float32),
        ('loin_depth', float32),
        ('loineye_area', float32),
        ('lean_percent', float32)
    ])

    @staticmethod
    def from_row(row: Tuple) -> Slaughter:
        return Slaughter(*map(from_ordinal, row[:2]), *row[2:])

    @staticmethod
    def to_row(record: Slaughter) -> Tuple:
        return (*map(to_ordinal, record[:2]), *record[2:])
