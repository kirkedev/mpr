from datetime import datetime
from typing import Tuple, NamedTuple, List, Optional as Maybe

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
    date = datetime.strptime("%Y-%m-%d", date),
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

# Lookup table for purchase type descriptions as declared in the HG201 report from the USDA
PURCHASE_TYPES = {
  'Prod. Sold Negotiated': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.CARCASS),
  'Prod. Sold Swine or Pork Market Formula': PurchaseType(Seller.PRODUCER, Arrangement.MARKET_FORMULA, Basis.CARCASS),
  'Prod. Sold Other Market Formula': PurchaseType(Seller.PRODUCER, Arrangement.OTHER_MARKET_FORMULA, Basis.CARCASS),
  'Prod. Sold Negotiated Formula': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),
  'Prod. Sold Other Purchase Arrangement': PurchaseType(Seller.PRODUCER, Arrangement.OTHER_PURCHASE, Basis.CARCASS),
  'Prod. Sold (All Purchase Types)': PurchaseType(Seller.PRODUCER, Arrangement.ALL, Basis.CARCASS),
  'Pack. Sold (All Purchase Types)': PurchaseType(Seller.PACKER, Arrangement.PACKER_SOLD, Basis.CARCASS),
  'Packer Owned': PurchaseType(Seller.PACKER, Arrangement.PACKER_OWNED, Basis.CARCASS)
}

def parse_line(line: List[str]) -> SlaughterRecord:
  """ Parses a line read from the daily Slaughtered Swine Report csv file into a SlaughterRecord """
  (_, date, purchase_type, head_count, base_price, net_price, low_price, high_price,
      live_weight, carcass_weight, *_, lean_percent) = line

  (seller, arrangement, basis) = PURCHASE_TYPES[purchase_type]

  return SlaughterRecord(
    date = datetime.strptime(date, "%m/%d/%Y"),
    seller = seller,
    arrangement = arrangement,
    basis = basis,
    head_count = int(head_count.replace(',', '')) if head_count else 0,
    base_price = float(base_price) if base_price else None,
    net_price = float(net_price) if net_price else None,
    low_price = float(low_price) if low_price else None,
    high_price = float(high_price) if high_price else None,
    live_weight = float(live_weight) if live_weight else None,
    carcass_weight = float(carcass_weight) if carcass_weight else None,
    lean_percent = float(lean_percent) if lean_percent else None)
