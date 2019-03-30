from typing import NamedTuple
from typing import Iterator

import numpy as np
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray

from mpr.date import date_type
from mpr.date import Date
from mpr.date import to_ordinal


class Slaughter(NamedTuple):
    date: Date
    report_date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    base_price: float32
    net_price: float32
    low_price: float32
    high_price: float32
    live_weight: float32
    carcass_weight: float32
    sort_loss: float32
    backfat: float32
    loin_depth: float32
    loineye_area: float32
    lean_percent: float32

    def __hash__(self) -> int:
        return hash((
            to_ordinal(self.date),
            to_ordinal(self.report_date),
            self.seller,
            self.arrangement,
            self.basis))

    def __eq__(self, other) -> bool:
        return isinstance(other, Slaughter) and hash(self) == hash(other) and np.allclose(self[5:], other[5:])

    @property
    def total_weight(self) -> float:
        return self.head_count * self.carcass_weight

    @property
    def total_value(self) -> float:
        return self.total_weight * self.net_price

    @property
    def avg_price(self) -> float:
        return self.total_value / self.total_weight


def to_array(records: Iterator[Slaughter]) -> recarray:
    return np.rec.array(list(records), dtype=np.dtype([
        ('date', date_type),
        ('report_date', date_type),
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
    ]))
