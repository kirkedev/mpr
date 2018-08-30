import csv
from datetime import datetime, timedelta
from typing import NamedTuple, Iterator
from datetime import date

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from data.hg201 import get_slaughter
from data.model.purchase_type import Arrangement, Seller
from data.model.slaughter import SlaughterRecord

from data.hg200 import get_purchases

class PriceTotal(NamedTuple):
  date: datetime
  total_weight: float
  total_value: float

(DATE, TOTAL_WEIGHT, TOTAL_VALUE) = PriceTotal._fields

(PRICE, PRICE_CHANGE, INDEX, INDEX_CHANGE) = ('price', 'price_change', 'index', 'index_change')

def filter_types(record: SlaughterRecord) -> bool:
  return record.seller == Seller.PRODUCER and \
    record.arrangement in (Arrangement.NEGOTIATED, Arrangement.MARKET_FORMULA, Arrangement.NEGOTIATED_FORMULA)

def cash_total(record: SlaughterRecord) -> PriceTotal:
  return PriceTotal(record.date, record.total_weight, record.total_value)

def compute_cash_index(records: Iterator[SlaughterRecord]) -> DataFrame:
  # filter all records by purchase type and compute total weight and total value of each
  cash_totals = map(cash_total, filter(filter_types, records))
  data = DataFrame.from_records(cash_totals, columns=PriceTotal._fields)

  # pivot by date and calculate total weight, total value, and weighted average price
  table = pd.pivot_table(data, index=DATE, values=[TOTAL_WEIGHT, TOTAL_VALUE], aggfunc=np.sum)
  table[PRICE] = table[TOTAL_VALUE] / table[TOTAL_WEIGHT]
  table[PRICE_CHANGE] = table[PRICE] - table[PRICE].shift(1)

  # compute daily cash index from two day sliding window of total value / total weight
  totals = table.rolling(2).sum().dropna()
  table[INDEX] = totals[TOTAL_VALUE] / totals[TOTAL_WEIGHT]
  table[INDEX_CHANGE] = table[INDEX] - table[INDEX].shift(1)

  return table.drop([TOTAL_VALUE, TOTAL_WEIGHT], axis=1)

def get_cash_index(start_date: date, end_date: date = date.today()) -> DataFrame:
  return compute_cash_index(get_slaughter(start_date, end_date))

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Calculate the CME Lean Hog Index')
  parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)

  days = parser.parse_args().days
  today = date.today()
  start_date = today - timedelta(days=days * 2)

  pd.options.display.precision = 2
  print(get_cash_index(start_date, today).tail(days))
