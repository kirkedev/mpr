from abc import ABC
from typing import Tuple

from numpy import dtype
from numpy import uint32
from numpy import float32
from tables.tableextension import Row

from ..date import to_ordinal
from ..date import from_ordinal
from ..observation import Observation

from .model import Cutout


class CutoutEntity(Observation[Cutout], ABC):
    schema = dtype([
        ('date', uint32),
        ('report_date', uint32),
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
        return Cutout(*map(from_ordinal, row[:2]), *row[2:])

    @staticmethod
    def to_row(record: Cutout) -> Tuple:
        return (*map(to_ordinal, record[:2]), *record[2:])
