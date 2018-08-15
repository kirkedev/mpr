import csv
from datetime import datetime
from typing import NamedTuple

import numpy as np
import pandas as pd

from data.purchase_type import Arrangement, Seller
from data.slaughter import SlaughterRecord, parse_line

class CashTotal(NamedTuple):
  date: datetime
  total_weight: float
  total_value: float

def filter_types(record: SlaughterRecord) -> bool:
  return record.seller == Seller.PRODUCER and \
    record.arrangement in (Arrangement.NEGOTIATED, Arrangement.MARKET_FORMULA, Arrangement.NEGOTIATED_FORMULA)

def cash_total(record: SlaughterRecord) -> CashTotal:
  return CashTotal(record.date, record.total_weight, record.total_value)

def get_cash_index():
  with open('data/csv/LM_HG201-Barrows_Gilts.csv') as csvfile:
    report = csv.reader(csvfile)

    # skip header
    next(report, None)

    # parse csv into structured data and remove unneeded purchase types
    records = filter(filter_types, map(parse_line, report))

    # compute total weight and total value of each filtered record
    cash_totals = map(cash_total, records)
    data = pd.DataFrame.from_records(cash_totals, columns=CashTotal._fields)

  # pivot by date and calculate total weight and value
  table = pd.pivot_table(data, index=['date'], values=['total_weight', 'total_value'], aggfunc=np.sum)

  # compute daily cash index from two day sliding window of total value / total weight
  totals = table.rolling(2).sum().dropna()
  totals['cash_index'] = np.divide(totals['total_value'], totals['total_weight'])

  return totals['cash_index']
