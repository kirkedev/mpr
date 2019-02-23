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

    @staticmethod
    def from_row(row: Row) -> Cutout:
        return Cutout(datetime64(date.fromordinal(row[0]), 'D'), *row[1:])

    @staticmethod
    def to_row(record: Cutout) -> Tuple:
        return (record[0].astype(date).toordinal(), *record[1:])
