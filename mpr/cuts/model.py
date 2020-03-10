from typing import NamedTuple
from typing import Iterator

from numpy import float32
from numpy import recarray
from numpy import allclose
from numpy import dtype
from numpy import rec
from numpy import uint32
from numpy import uint8

from . import CutType
from ..data import Date
from ..data import date64
from ..data import date_ordinal
from ..data import unicode


class Cut(NamedTuple):
    report: str
    date: Date
    report_date: Date
    type: CutType
    description: str
    weight: uint32
    avg_price: float32
    low_price: float32
    high_price: float32

    def __hash__(self) -> int:
        return hash((self[0], *map(date_ordinal, self[1:3]), *self[3:5]))

    def __eq__(self, other) -> bool:
        return (isinstance(other, Cut) and hash(self) == hash(other) and
            allclose(self[6:], other[6:], equal_nan=True))


def to_array(records: Iterator[Cut]) -> recarray:
    return rec.array(list(records), dtype=dtype([
        ('report', unicode(8)),
        ('date', date64),
        ('report_date', date64),
        ('type', uint8),
        ('description', unicode(64)),
        ('weight', uint32),
        ('avg_price', float32),
        ('low_price', float32),
        ('high_price', float32)
    ]))
