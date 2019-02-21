from abc import ABC
from typing import Tuple
from datetime import date

from numpy import dtype
from numpy import datetime64
from numpy import uint32
from numpy import float32
from tables.tableextension import Row

from mpr.data.model.cutout import Cutout
from .observation import Observation


class CutoutEntity(Observation[Cutout], ABC):
    schema = dtype([
        ('date', uint32),
        ('primal_loads', float32),
        ('trimming_loads', float32),
        ('carcass_price', float32),
        ('loin_price', float32),
        ('butt_price', float32),
        ('picnic_price', float32),
        ('rib_price', float32),
        ('ham_price', float32),
        ('belly_price', float32)
    ])

    @classmethod
    def from_row(cls, row: Row) -> Cutout:
        return Cutout(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            primal_loads=row['primal_loads'],
            trimming_loads=row['trimming_loads'],
            carcass_price=row['carcass_price'],
            loin_price=row['loin_price'],
            butt_price=row['butt_price'],
            picnic_price=row['picnic_price'],
            rib_price=row['rib_price'],
            ham_price=row['ham_price'],
            belly_price=row['belly_price'])

    @staticmethod
    def to_row(record: Cutout) -> Tuple:
        return (
            record.date.astype(date).to_ordinal(),
            record.primal_loads,
            record.trimming_loads,
            record.carcass_price,
            record.loin_price,
            record.butt_price,
            record.picnic_price,
            record.rib_price,
            record.ham_price,
            record.belly_price)
