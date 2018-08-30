import csv
from datetime import datetime, timedelta
from typing import NamedTuple, Iterator
from datetime import date

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from data.api.slaughter import get_slaughter, Record as SlaughterRecord

def filter_types(record: SlaughterRecord) -> bool:
  return record.purchase_type in ('Prod. Sold Negotiated', 'Prod. Sold Negotiated Formula',
    'Prod. Sold Swine or Pork Market Formula')

def compute_weight(head_count: Series, carcass_weight: Series) -> Series:
  return (head_count * carcass_weight).rename('total_weight')

def compute_value(total_weight: Series, net_price: Series) -> Series:
  return (total_weight * net_price).rename('total_value')

def compute_price(total_value: Series, total_weight: Series) -> Series:
  return (total_value / total_weight).rename('weighted_price')

def compute_cash_index(records: Iterator[SlaughterRecord]) -> DataFrame:
  slaughter = DataFrame.from_records(records, columns=SlaughterRecord._fields)

  slaughter['purchase_type'] = slaughter['purchase_type'].replace({
    'Prod. Sold Negotiated': 'Negotiated',
    'Prod. Sold Swine or Pork Market Formula': 'Market Formula',
    'Prod. Sold Negotiated Formula': 'Negotiated Formula'
  })

  slaughter = slaughter.set_index(['date', 'purchase_type'])

  total_weight = compute_weight(slaughter['head_count'], slaughter['carcass_weight'])
  total_value = compute_value(total_weight, slaughter['net_price'])
  price = compute_price(total_value, total_weight)

  totals = pd.pivot_table(pd.concat([total_weight, total_value], axis=1), index='date')
  daily_price = compute_price(totals['total_value'], totals['total_weight'])
  rolling_totals = totals.rolling(2).sum().dropna()
  cme_index = compute_price(rolling_totals['total_value'], rolling_totals['total_weight']).rename('cme_index')

  table = pd.concat([slaughter['head_count'], slaughter['carcass_weight'], price], axis=1).unstack()
  cols = [(col, purchase_type) for (col, purchase_type) in table.columns if purchase_type != 'Negotiated Formula']
  table = table[cols]

  price_change = (daily_price - daily_price.shift(1)).rename('price_change')
  index_change = (cme_index - cme_index.shift(1)).rename('index_change')

  return pd.concat([table, daily_price, price_change, cme_index, index_change], axis=1)

def get_cash_prices(days: int) -> DataFrame:
  return compute_cash_index(filter(filter_types, get_slaughter(days + 2))).tail(days)

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Calculate the CME Lean Hog Index')
  parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)
  days = parser.parse_args().days

  print(get_cash_prices(days))
