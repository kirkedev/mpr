from typing import Tuple
from typing import Iterator
from typing import Set
from datetime import date

import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas.tseries.holiday import Holiday
from pandas.tseries.holiday import USMemorialDay
from pandas.tseries.holiday import USLaborDay
from pandas.tseries.holiday import USThanksgivingDay
from pandas.tseries.holiday import nearest_workday
from pandas.tseries.offsets import CustomBusinessDay

DateInterval = Tuple[date, date]


def date_range(start: date, end: date) -> Iterator[date]:
    return map(date.fromordinal, range(start.toordinal(), end.toordinal() + 1))


def date_diff(first: Iterator[date], second: Iterator[date]) -> Set[date]:
    return set(second) - set(first)


USIndependenceDayBefore2009 = Holiday('US Independence Day',
    month=7,
    day=4,
    end_date='2009-07-01',
    observance=nearest_workday)

USIndependenceDayAfter2009 = Holiday('US Independence Day',
    month=7,
    day=4,
    start_date='2010-07-01',
    observance=nearest_workday)

NewYearsDay = Holiday('New Years Day', month=1, day=1, observance=nearest_workday)
ChristmasEve = Holiday('Christmas Eve', month=12, day=24)
Christmas = Holiday('Christmas', month=12, day=25, observance=nearest_workday)

MartinLutherKingDay2013 = date(2013, 1, 21)
PresidentsDay2013 = date(2013, 2, 18)
GovernmentShutdown2013 = date_range(date(2013, 10, 1), date(2013, 10, 17))

report_calendar = AbstractHolidayCalendar(rules=[
    NewYearsDay,
    USMemorialDay,
    USIndependenceDayBefore2009,
    USIndependenceDayAfter2009,
    USLaborDay,
    USThanksgivingDay,
    ChristmasEve,
    Christmas
])

report_date = CustomBusinessDay(normalize=True, calendar=report_calendar, holidays=[
    MartinLutherKingDay2013,
    PresidentsDay2013,
    *GovernmentShutdown2013
])


def report_date_range(start: date, end: date) -> Iterator[date]:
    return map(lambda it: it.date(), pd.date_range(start=start, end=end, freq=report_date))


def recent_report_dates(days: int) -> Iterator[date]:
    return map(lambda it: it.date(), pd.date_range(end=date.today(), periods=days, freq=report_date))


def report_date_intervals(dates: Set[date]) -> Iterator[DateInterval]:
    dates = sorted(dates)

    if len(dates) == 0:
        return []

    start = previous_date = dates[0]

    for current_date in dates[1:]:
        next_date = (previous_date + report_date).date()

        if current_date == next_date:
            previous_date = current_date
        else:
            yield start, previous_date
            start = previous_date = current_date

    yield start, previous_date
