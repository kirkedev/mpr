from abc import ABC
from typing import Tuple
from datetime import date

from numpy import dtype
from numpy import datetime64
from numpy import uint8
from numpy import uint32
from numpy import float32
from tables.tableextension import Row

from mpr.model.slaughter import Slaughter
from .observation import Observation


class SlaughterEntity(Observation[Slaughter], ABC):
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
    def from_row(row: Row) -> Slaughter:
        return Slaughter(
            datetime64(date.fromordinal(row[0]), 'D'),
            datetime64(date.fromordinal(row[1]), 'D'),
            *row[2:])

    @staticmethod
    def to_row(record: Slaughter) -> Tuple:
        return (
            record[0].astype(date).toordinal(),
            record[1].astype(date).toordinal(),
            *record[2:])
