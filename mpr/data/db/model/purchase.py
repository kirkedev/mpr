from datetime import date
from dataclasses import dataclass
from typing import Optional

from tables import UInt32Col, Float32Col
from tables.tableextension import Row

from .model import Observation
from .purchase_type import PurchaseTypeCol, Seller, Arrangement, Basis

@dataclass
class Purchase(Observation):
  """
  Aggregate data structure for pricing of purchased barrows and gilts per date and purchase type, as
  retrieved from a USDA purchased swine report (LMHG201 - Prior Day, LM_HG202 - Morning, and LM_HG203 - Afternoon)
  https://www.ams.usda.gov/mnreports/lm_hg202.txt
  """

  date: date
  seller: Seller
  arrangement: Arrangement
  basis: Basis
  head_count: int
  avg_price: Optional[float]
  low_price: Optional[float]
  high_price: Optional[float]

  schema = {
    'date': UInt32Col(),
    'purchase_type': PurchaseTypeCol(),
    'head_count': UInt32Col(),
    'avg_price': Float32Col(),
    'low_price': Float32Col(),
    'high_price': Float32Col()
  }

  @classmethod
  def from_row(cls, row: Row) -> 'Purchase':
    return cls(
      date = date.fromordinal(row['date']),
      seller = Seller.from_ordinal(row['purchase_type/seller']),
      arrangement = Arrangement.from_ordinal(row['purchase_type/arrangement']),
      basis = Basis.from_ordinal(row['purchase_type/basis']),
      head_count = row['head_count'],
      avg_price = row['avg_price'],
      low_price = row['low_price'],
      high_price = row['high_price'])

  def append(self):
    row = self.table.row

    row['date'] = self.date.toordinal()
    row['purchase_type/seller'] = self.seller.to_ordinal()
    row['purchase_type/arrangement'] = self.arrangement.to_ordinal()
    row['purchase_type/basis'] = self.basis.to_ordinal()
    row['head_count'] = self.head_count
    row['avg_price'] = self.avg_price
    row['low_price'] = self.low_price
    row['high_price'] = self.high_price

    row.append()
