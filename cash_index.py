import csv
from datetime import datetime, timedelta
from typing import NamedTuple, Iterator
from datetime import date

import numpy as np
import pandas as pd

from data.hg201 import get_slaughter
from data.model.purchase_type import Arrangement, Seller
from data.model.slaughter import SlaughterRecord

class CashTotal(NamedTuple):
  date: datetime
  total_weight: float
  total_value: float

(DATE, TOTAL_WEIGHT, TOTAL_VALUE) = CashTotal._fields

def filter_types(record: SlaughterRecord) -> bool:
  return record.seller == Seller.PRODUCER and \
    record.arrangement in (Arrangement.NEGOTIATED, Arrangement.MARKET_FORMULA, Arrangement.NEGOTIATED_FORMULA)

def cash_total(record: SlaughterRecord) -> CashTotal:
  return CashTotal(record.date, record.total_weight, record.total_value)

def compute_cash_index(records: Iterator[SlaughterRecord]) -> pd.DataFrame:
  # filter all records by purchase type and compute total weight and total value of each
  cash_totals = map(cash_total, filter(filter_types, records))
  data = pd.DataFrame.from_records(cash_totals, columns=CashTotal._fields)

  # pivot by date and calculate total weight, total value, and weighted average price
  table = pd.pivot_table(data, index=DATE, values=[TOTAL_WEIGHT, TOTAL_VALUE], aggfunc=np.sum)
  table['weighted_price'] = table[TOTAL_VALUE] / table[TOTAL_WEIGHT]

  # compute daily cash index from two day sliding window of total value / total weight
  totals = table.rolling(2).sum().dropna()
  table['cash_index'] = totals[TOTAL_VALUE] / totals[TOTAL_WEIGHT]

  return table.drop([TOTAL_VALUE, TOTAL_WEIGHT], axis=1)

def get_cash_index(start_date: date, end_date: date = date.today()):
  return compute_cash_index(get_slaughter(start_date, end_date))

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Calculate the CME Lean Hog Index')
  parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=5)

  days = parser.parse_args().days
  today = date.today()
  start_date = today - timedelta(days=days * 2)

  pd.options.display.precision = 2
  print(get_cash_index(start_date, today).tail(days))
