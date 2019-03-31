from typing import Union
from typing import Tuple
from typing import Iterator
from typing import List
from enum import Enum
from datetime import date

import pandas as pd
from pandas import Series
from pandas import DataFrame

from .calendar import DateInterval
from .calendar import date_diff
from .calendar import recent_report_dates
from .calendar import report_date_range
from .calendar import report_date_intervals

pd.options.display.float_format = '{:,.2f}'.format


class Report(Enum):
    PURCHASED_SWINE = 'lm_hg200'
    SLAUGHTERED_SWINE = 'lm_hg201'
    DIRECT_HOG_MORNING = 'lm_hg202'
    DIRECT_HOG_AFTERNOON = 'lm_hg203'
    CUTOUT_MORNING = 'lm_pk600'
    CUTOUT_AFTERNOON = 'lm_pk602'


def request_range(start: date, end: date, dates: Iterator[date]) -> List[DateInterval]:
    return list(report_date_intervals(date_diff(dates, report_date_range(start, end))))


def request_recent_reports(days: int) -> List[DateInterval]:
    return list(report_date_intervals(date_diff([], recent_report_dates(days))))


def compute_change(values: Series) -> Series:
    return values - values.shift(1)


def with_change(values: Series) -> Tuple[Series, Series]:
    values = values.round(decimals=2)
    return values, compute_change(values)


def create_table(*columns: Union[Series, DataFrame]) -> DataFrame:
    return pd.concat(columns, axis=1)
