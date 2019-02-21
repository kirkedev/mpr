from abc import ABC
from typing import Tuple
from datetime import date

from numpy import dtype
from numpy import datetime64
from numpy import uint8
from numpy import uint32
from numpy import float32
from tables.tableextension import Row

from mpr.data.model.slaughter import Slaughter
from .observation import Observation


class SlaughterEntity(Observation[Slaughter], ABC):
    schema = dtype([
        ('date', uint32),
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

    @classmethod
    def from_row(cls, row: Row) -> Slaughter:
        return Slaughter(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            seller=row['seller'],
            arrangement=row['arrangement'],
            basis=row['basis'],
            head_count=row['head_count'],
            base_price=row['base_price'],
            net_price=row['net_price'],
            low_price=row['low_price'],
            high_price=row['high_price'],
            live_weight=row['live_weight'],
            carcass_weight=row['carcass_weight'],
            sort_loss=row['sort_loss'],
            backfat=row['backfat'],
            loin_depth=row['loin_depth'],
            loineye_area=row['loineye_area'],
            lean_percent=row['lean_percent'])

    @staticmethod
    def to_row(record: Slaughter) -> Tuple:
        return (
            record.date.astype(date).toordinal(),
            record.seller,
            record.arrangement,
            record.basis,
            record.head_count,
            record.base_price,
            record.net_price,
            record.low_price,
            record.high_price,
            record.live_weight,
            record.carcass_weight,
            record.sort_loss,
            record.backfat,
            record.loin_depth,
            record.loineye_area,
            record.lean_percent)
