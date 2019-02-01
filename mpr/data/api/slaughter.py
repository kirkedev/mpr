from enum import Enum
from functools import singledispatch
from typing import NamedTuple, Optional, Iterator
from datetime import date, datetime, timedelta

from .api import fetch, opt_float, opt_int, date_interval, Report, Attributes

date_format = "%m/%d/%Y"

class Section(Enum):
  # SUMMARY = 'Summary'
  BARROWS_AND_GILTS = 'Barrows/Gilts'
  # CARCASS_MEASUREMENTS = 'Carcass Measurements'
  # SOWS_AND_BOARS = 'Sows/Boars'
  # SCHEDULED_SWINE = '14-Day Scheduled Swine'
  # NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'

class Record(NamedTuple):
  date: date
  report_date: date
  purchase_type: str
  head_count: int
  base_price: Optional[float]
  net_price: Optional[float]
  low_price: Optional[float]
  high_price: Optional[float]
  live_weight: Optional[float]
  carcass_weight: Optional[float]
  sort_loss: Optional[float]
  backfat: Optional[float]
  loin_depth: Optional[float]
  loineye_area: Optional[float]
  lean_percent: Optional[float]

def parse_attributes(attr: Attributes) -> Record:
  date = attr['for_date_begin']
  report_date = attr['report_date']
  purchase_type = attr['purchase_type']

  return Record(
    date = datetime.strptime(date, date_format),
    report_date = datetime.strptime(report_date, date_format),
    purchase_type = purchase_type,
    head_count = opt_int(attr, 'head_count') or 0,
    base_price = opt_float(attr, 'base_price'),
    net_price = opt_float(attr, 'avg_net_price'),
    low_price = opt_float(attr, 'lowest_net_price'),
    high_price = opt_float(attr, 'highest_net_price'),
    live_weight = opt_float(attr, 'avg_live_weight'),
    carcass_weight = opt_float(attr, 'avg_carcass_weight'),
    sort_loss = opt_float(attr, 'avg_sort_loss'),
    backfat = opt_float(attr, 'avg_backfat'),
    loin_depth = opt_float(attr, 'avg_loin_depth'),
    loineye_area = opt_float(attr, 'loineye_area'),
    lean_percent = opt_float(attr, 'avg_lean_percent'))

@singledispatch
async def get_slaughter(start_date: date, end_date=date.today()) -> Iterator[Record]:
  response = await fetch(Report.SLAUGHTERED_SWINE, start_date + timedelta(days=1), end_date)

  return (parse_attributes(attr) for attr in response
    if attr['label'] == Section.BARROWS_AND_GILTS.value)

@get_slaughter.register(int)
async def get_slaughter_days(days: int) -> Iterator[Record]:
  return await get_slaughter(*date_interval(days))

lm_hg201 = hg201 = get_slaughter

if __name__ == "__main__":
  import pandas as pd
  data = pd.DataFrame.from_records(lm_hg201(10), columns=Record._fields, index='date')

  print(data)
