from datetime import date, datetime
from typing import Tuple, NamedTuple, List, Optional as Maybe
from tables import IsDescription, Time32Col, EnumCol, UInt8Col, UInt16Col, UInt32Col

from .purchase_type import PurchaseType, Seller, Arrangement, Basis

class PurchaseRecord(NamedTuple):
  """ Aggregate data structure for pricing of purchased barrows and gilts per date and purchase type, as
      retrieved from a USDA purchased swine report (LMHG201, LM_HG202, and LM_HG203)
      https://www.ams.usda.gov/mnreports/lm_hg202.txt """

  date: date
  seller: Seller
  arrangement: Arrangement
  basis: Basis
  head_count: int
  avg_price: Maybe[float]
  low_price: Maybe[float]
  high_price: Maybe[float]

# Type alias to represent a row in a sqlite3 table of purchase records
Row = Tuple[str, str, str, int, Maybe[float], Maybe[float], Maybe[float]]

PURCHASE_TYPES = {
  'Negotiated (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.CARCASS),
  'Negotiated Formula (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),
  'Swine/Pork Market Formula (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.MARKET_FORMULA, Basis.CARCASS),
  'Negotiated (live basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.LIVE),
  'Negotiated Formula (live basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.LIVE),
  'Combined Negotiated/Negotiated Formula (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.ALL_NEGOTIATED, Basis.CARCASS),
  'Combined Negotiated/Negotiated Formula (live basis)': PurchaseType(Seller.PRODUCER, Arrangement.ALL_NEGOTIATED, Basis.LIVE),
}

def parse_line(line: List[str]) -> PurchaseRecord:
  """ Parses a line read from the daily Purchased Swine Report csv file into a PurchaseRecord """
  (_, date, purchase_type, head_count, low_price, high_price, avg_price, _) = line

  (seller, arrangement, basis) = PURCHASE_TYPES[purchase_type]

  return PurchaseRecord(
    date = datetime.strptime(date, "%m/%d/%Y").date(),
    seller = seller,
    arrangement = arrangement,
    basis = basis,
    head_count = int(head_count.replace(',', '')) if head_count else 0,
    avg_price = float(avg_price) if avg_price else None,
    low_price = float(low_price) if low_price else None,
    high_price = float(high_price) if high_price else None)
