from datetime import datetime
from typing import Tuple, NamedTuple, Iterable, Iterator, Optional as Maybe
from datetime import date, timedelta

from .purchase_type import PurchaseType, Seller, Arrangement, Basis

class SlaughterRecord(NamedTuple):
  """ Aggregate data structure for pricing and weights of slaughtered barrows and gilts per date and purchase type.
      Data is retrieved from the USDA's daily Slaughtered Swine Report (LM_HG201)
      https://www.ams.usda.gov/mnreports/lm_hg201.txt """

  date: datetime
  seller: Seller
  arrangement: Arrangement
  basis: Basis
  head_count: int
  base_price: Maybe[float]
  net_price: Maybe[float]
  low_price: Maybe[float]
  high_price: Maybe[float]
  live_weight: Maybe[float]
  carcass_weight: Maybe[float]
  lean_percent: Maybe[float]

  @property
  def total_weight(self) -> float:
    return self.head_count * self.carcass_weight if self.carcass_weight else 0.0

  @property
  def total_value(self) -> float:
    return self.total_weight * self.net_price if self.net_price else 0.0

# Type alias to represent a row in a sqlite3 table of slaughter records
Row = Tuple[str, str, str, int, Maybe[float], Maybe[float], Maybe[float], Maybe[float], Maybe[float], Maybe[float], Maybe[float]]

def from_cursor(row: Row) -> SlaughterRecord:
  """ Creates a new SlaughterRecord out of a Row fetched from a sqlite3 table """
  (date, seller, arrangement, head_count,
      base_price, net_price, low_price, high_price, live_weight, carcass_weight, lean_percent) = row

  return SlaughterRecord(
    date = datetime.strptime(date, "%Y-%m-%d"),
    seller = Seller(seller),
    arrangement = Arrangement(arrangement),
    basis = Basis.CARCASS,
    head_count = head_count,
    base_price = base_price,
    net_price = net_price,
    low_price = low_price,
    high_price = high_price,
    live_weight = live_weight,
    carcass_weight = carcass_weight,
    lean_percent = lean_percent)
