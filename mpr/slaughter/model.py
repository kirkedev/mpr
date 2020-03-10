from typing import NamedTuple
from typing import Iterator

from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray
from numpy import allclose
from numpy import dtype
from numpy import rec

from ..data import date64
from ..data import Date
from ..data import date_ordinal
from ..data import unicode


class Slaughter(NamedTuple):
    report: str
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
        return hash((self[0], *map(date_ordinal, self[1:3]), self[3:6]))

    def __eq__(self, other) -> bool:
        return (isinstance(other, Slaughter) and hash(self) == hash(other) and
            allclose(self[6:], other[6:], equal_nan=True))

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
    return rec.array(list(records), dtype=dtype([
        ('report', unicode(8)),
        ('date', date64),
        ('report_date', date64),
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
