from datetime import date
from datetime import datetime
from typing import Dict
from typing import Iterator
from typing import Optional

from dateutil.tz import gettz
from isoweek import Week
from numpy import datetime64
from numpy import dtype
from numpy import float32
from numpy import nan
from numpy import uint32

date64 = dtype('datetime64[D]')
Date = type(date64)
Record = Dict[str, str]


def unicode(length: int) -> dtype:
    return dtype(f"U{length}")


def strip_commas(value: str) -> str:
    return value.replace(',', '')


def get_optional(record: Record, key: str) -> Optional[str]:
    return record[key] if key in record and record[key] != 'null' else None


def opt_float(record: Record, key: str) -> float32:
    value = get_optional(record, key)
    return float32(strip_commas(value)) if value else nan


def opt_int(record: Record, key: str) -> uint32:
    value = get_optional(record, key)
    return uint32(strip_commas(value)) if value else 0


def chicago_time(hour: Optional[int] = None) -> datetime:
    result = datetime.now(gettz('America/Chicago'))
    return result if hour is None else result.replace(hour=hour, minute=0, second=0, microsecond=0)


def record_date(record: Record) -> date:
    return datetime.strptime(record['report_date'], "%m/%d/%Y").date()


def parse_date(date_string: str, date_format: str) -> date64:
    return datetime64(datetime.strptime(date_string, date_format).date(), 'D')


def weeks(start: date, end: date) -> Iterator[Week]:
    for week in range(Week.withdate(start).toordinal(), Week.withdate(end).toordinal() + 1):
        yield Week.fromordinal(week)
