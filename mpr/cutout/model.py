from typing import NamedTuple
from typing import Iterator

import numpy as np
from numpy import float32
from numpy import recarray

from ..date import Date
from ..date import date_type
from ..date import to_ordinal


class Cutout(NamedTuple):
    date: Date
    report_date: Date
    primal_loads: float32
    trimming_loads: float32
    carcass_price: float32
    loin_price: float32
    butt_price: float32
    picnic_price: float32
    rib_price: float32
    ham_price: float32
    belly_price: float32

    def __hash__(self) -> int:
        return hash((to_ordinal(self.date), to_ordinal(self.report_date)))

    def __eq__(self, other) -> bool:
        return isinstance(other, Cutout) and hash(self) == hash(other) and \
            np.allclose(self[2:], other[2:], equal_nan=True)

    @property
    def loads(self):
        return self.primal_loads + self.trimming_loads

    @property
    def value(self):
        return self.loads * self.carcass_price


def to_array(records: Iterator[Cutout]) -> recarray:
    return np.rec.array(list(records), dtype=np.dtype([
        ('date', date_type),
        ('report_date', date_type),
        ('primal_loads', float32),
        ('trimming_loads', float32),
        ('carcass_price', float32),
        ('loin_price', float32),
        ('butt_price', float32),
        ('picnic_price', float32),
        ('rib_price', float32),
        ('ham_price', float32),
        ('belly_price', float32)
    ]))
