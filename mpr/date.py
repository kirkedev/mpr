from typing import Tuple
from datetime import date
from datetime import datetime

from numpy import dtype
from numpy import uint32
from numpy import datetime64

date64 = dtype('datetime64[D]')
Date = type(date64)
DateInterval = Tuple[date, date]


def to_ordinal(dt: date64) -> uint32:
    return dt.astype(date).toordinal()


def from_ordinal(ordinal: uint32) -> date64:
    return datetime64(date.fromordinal(ordinal), 'D')


def from_string(date_string: str, date_format: str) -> date64:
    return datetime64(datetime.strptime(date_string, date_format).date(), 'D')


def quarter(year: int, ordinal: int) -> DateInterval:
    month = ordinal * 3 + 1
    start = date(year, month, 1)
    end = date(year, month + 3, 1) if 0 <= ordinal < 3 else date(year + 1, 1, 1)
    return start, end


def get_quarter(of: date) -> int:
    return (of.month - 1) // 3
