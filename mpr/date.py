from typing import Tuple
from datetime import date
from datetime import datetime

from numpy import dtype
from numpy import uint32
from numpy import datetime64

date64 = dtype('datetime64[D]')
Date = type(date64)
DateInterval = Tuple[date, date]


def from_string(date_string: str, date_format: str) -> date64:
    return datetime64(datetime.strptime(date_string, date_format).date(), 'D')


def to_ordinal(it: date64) -> uint32:
    return it.astype(date).toordinal()


def from_ordinal(ordinal: uint32) -> date64:
    return datetime64(date.fromordinal(ordinal), 'D')
