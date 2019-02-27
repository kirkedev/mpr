from typing import Iterator
from typing import List
from enum import Enum
from datetime import date

from .report_calendar import DateInterval
from .report_calendar import date_diff
from .report_calendar import recent_report_dates
from .report_calendar import report_date_range
from .report_calendar import report_date_intervals


class Report(Enum):
    PURCHASED_SWINE = 'lm_hg200'
    SLAUGHTERED_SWINE = 'lm_hg201'
    DIRECT_HOG_MORNING = 'lm_hg202'
    DIRECT_HOG_AFTERNOON = 'lm_hg203'
    CUTOUT_MORNING = 'lm_pk602'
    CUTOUT_AFTERNOON = 'lm_pk603'


def request_range(start: date, end: date, dates: Iterator[date]) -> List[DateInterval]:
    return list(report_date_intervals(date_diff(dates, report_date_range(start, end))))


def request_recent_reports(days: int) -> List[DateInterval]:
    return list(report_date_intervals(date_diff([], recent_report_dates(days))))
