from datetime import date
from datetime import datetime

from numpy import dtype
from numpy import uint32
from numpy import datetime64

date_type = dtype('datetime64[D]')
Date = type(date_type)


def to_ordinal(dt: date_type) -> uint32:
    return dt.astype(date).toordinal()


def from_ordinal(ordinal: uint32) -> date_type:
    return datetime64(date.fromordinal(ordinal), 'D')


def from_string(date_string: str, date_format: str) -> date_type:
    return datetime64(datetime.strptime(date_string, date_format).date(), 'D')
