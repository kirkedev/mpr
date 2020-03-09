from typing import NamedTuple
from typing import Iterator

from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray
from numpy import allclose
from numpy import dtype
from numpy import rec

from ..date import date64
from ..date import Date
from ..date import to_ordinal


class Purchase(NamedTuple):
    report: str
    date: Date
    report_date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32

    def __hash__(self) -> int:
        return hash((self[0], *map(to_ordinal, self[1:3]), *self[3:6]))

    def __eq__(self, other) -> bool:
        return (isinstance(other, Purchase) and hash(self) == hash(other) and
            allclose(self[6:], other[6:], equal_nan=True))


def to_array(records: Iterator[Purchase]) -> recarray:
    return rec.array(list(records), dtype=dtype([
        ('report', dtype('U8')),
        ('date', date64),
        ('report_date', date64),
        ('seller', uint8),
        ('arrangement', uint8),
        ('basis', uint8),
        ('head_count', uint32),
        ('avg_price', float32),
        ('low_price', float32),
        ('high_price', float32)
    ]))
