from typing import NamedTuple
from typing import Iterator
from datetime import date

import numpy as np
from numpy import float32
from numpy import recarray

from . import Date
from . import date_type


class Cutout(NamedTuple):
    date: Date
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
        return hash(self.date.astype(date).toordinal())

    def __eq__(self, other) -> bool:
        return isinstance(other, Cutout) and hash(self) == hash(other) and np.allclose(self[1:], other[1:])


def to_array(records: Iterator[Cutout]) -> recarray:
    return np.rec.array(list(records), dtype=np.dtype([
        ('date', date_type),
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
