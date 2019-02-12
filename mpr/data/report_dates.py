from datetime import date
from typing import Tuple, Optional, Iterator, List, Type, TypeVar
from itertools import tee
from bisect import bisect_left

import numpy as np
from db.model.model import Observation

DateInterval = Tuple[date, date]

def business_days(current: date, end: date, step=1) -> Iterator[date]:
  holidays = [
    '2018-01-01',
    '2018-05-28',
    '2018-09-03',
    '2018-12-25'
  ]

  current = np.busday_offset(current, 0, roll='forward', holidays=holidays)

  while current <= end:
    yield current.astype('O')
    current = np.busday_offset(current, step, roll='forward', holidays=holidays)

T = TypeVar('T')
def contains(items: List[T], item: T) -> bool:
  if len(items) < 30:
    return item in items

  i = bisect_left(items, item)
  return i < len(items) and items[i] == item

def find_next(dates: Iterator[date], observation_dates: Iterator[date]) -> Optional[date]:
  a, b = tee(dates)
  last = next(b, None)

  for last, current in zip(a, b):
    if contains(observation_dates, current):
      return last

  return last

def date_intervals(start: date, end: date, model: Type[Observation]) -> Iterator[DateInterval]:
  observation_dates = model.dates()

  if len(observation_dates) == 0:
    yield start, end
    return

  i0 = bisect_left(observation_dates, start)
  i1 = bisect_left(observation_dates, end) + 1
  observation_dates = observation_dates[i0:i1]

  dates = business_days(start, end)

  for report_date in dates:
    if not contains(observation_dates, report_date):
      next_date = find_next(dates, observation_dates)
      yield report_date, (next_date if next_date is not None else report_date)
