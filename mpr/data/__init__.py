from typing import Tuple
from typing import Iterator
from enum import Enum
from datetime import date

import numpy as np

DateInterval = Tuple[date, date]


class Report(Enum):
    PURCHASED_SWINE = 'lm_hg200'
    SLAUGHTERED_SWINE = 'lm_hg201'
    DIRECT_HOG_MORNING = 'lm_hg202'
    DIRECT_HOG_AFTERNOON = 'lm_hg203'
    CUTOUT_MORNING = 'lm_pk602'
    CUTOUT_AFTERNOON = 'lm_pk603'


def date_range(start: date, end: date) -> Iterator[date]:
    return map(date.fromordinal, range(start.toordinal(), end.toordinal() + 1))


def date_diff(first: Iterator[date], second: Iterator[date]) -> Iterator[date]:
    return filter(np.is_busday, set(second) - set(first))


def date_intervals(dates: Iterator[date]) -> Iterator[DateInterval]:
    dates = sorted(set(dates))

    if len(dates) == 0:
        return []

    start = previous_date = dates[0]

    for date in dates[1:]:
        if date == np.busday_offset(previous_date, 1):
            previous_date = date
        else:
            yield start, previous_date
            start = previous_date = date

    yield start, previous_date
