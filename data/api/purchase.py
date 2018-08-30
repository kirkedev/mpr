from enum import Enum
from typing import NamedTuple, Optional, Iterator
from datetime import date, datetime, timedelta
from functools import singledispatch

from api import fetch, parse_elements, opt_float, opt_int, date_interval, Report, Attributes

date_format = "%m/%d/%Y"

class Section(Enum):
  # VOLUME = 'Current Volume by Purchase Type'
  BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
  # CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
  # CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
  # AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
  # SOWS = 'Sows'
  # STATES = 'State of Origin'

class Record(NamedTuple):
  date: date
  purchase_type: str
  head_count: int
  avg_price: Optional[float]
  low_price: Optional[float]
  high_price: Optional[float]

def parse_attributes(attr: Attributes) -> Record:
  date = attr.get('reported_for_date') or attr['report_date']
  purchase_type = attr['purchase_type']

  return Record(
    date = datetime.strptime(date, date_format).date(),
    purchase_type = purchase_type,
    head_count = opt_int(attr, 'head_count') or 0,
    avg_price = opt_float(attr, 'wtd_avg'),
    low_price = opt_float(attr, 'price_low'),
    high_price = opt_float(attr, 'price_high'))

@singledispatch
def get_prior_day(start_date: date, end_date: date=date.today()) -> Iterator[Record]:
  response = fetch(Report.PURCHASED_SWINE, start_date + timedelta(days = 1), end_date)

  return (parse_attributes(attr) for attr in parse_elements(response)
    if attr['label'] == Section.BARROWS_AND_GILTS.value)

@get_prior_day.register(int)
def get_prior_days(days: int) -> Iterator[Record]:
  return get_prior_day(*date_interval(days))

@singledispatch
def get_morning(start_date: date, end_date: date=date.today()) -> Iterator[Record]:
  response = fetch(Report.DIRECT_HOG_MORNING, start_date, end_date)

  return (parse_attributes(attr) for attr in parse_elements(response)
    if attr['label'] == Section.BARROWS_AND_GILTS.value)

@get_morning.register(int)
def get_morning_days(days: int) -> Iterator[Record]:
  return get_morning(*date_interval(days))

@singledispatch
def get_afternoon(start_date: date, end_date: date=date.today()) -> Iterator[Record]:
  response = fetch(Report.DIRECT_HOG_AFTERNOON, start_date, end_date)

  return (parse_attributes(attr) for attr in parse_elements(response)
    if attr['label'] == Section.BARROWS_AND_GILTS.value)

@get_afternoon.register(int)
def get_afternoon_days(days: int) -> Iterator[Record]:
  return get_afternoon(*date_interval(days))

lm_hg200 = hg200 = get_prior_day
lm_hg202 = hg202 = get_morning
lm_hg203 = hg203 = get_afternoon

if __name__ == "__main__":
  import pandas as pd
  data = pd.DataFrame.from_records(lm_hg200(10), columns=Record._fields, index='date')

  print(data)
