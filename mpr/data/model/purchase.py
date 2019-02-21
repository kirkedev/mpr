from typing import NamedTuple
from typing import Iterator

import numpy as np
from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import recarray

from . import date_type
from . import Date


class Purchase(NamedTuple):
    date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32


dtype = np.dtype([
    ('date', date_type),
    ('seller', uint8),
    ('arrangement', uint8),
    ('basis', uint8),
    ('head_count', uint32),
    ('avg_price', float32),
    ('low_price', float32),
    ('high_price', float32)
])


def to_array(records: Iterator[Purchase]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
