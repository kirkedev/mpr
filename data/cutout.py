from datetime import datetime
from typing import Tuple, NamedTuple, List

class CutoutRecord(NamedTuple):
  """ Aggregate data structure for pricing of primal pork cuts, as retrieved from the
      USDA Daily Pork reports (LM_PK602, LM_PK603) """

  date: datetime
  primal_loads: float
  trimming_loads: float
  carcass_price: float
  loin_price: float
  butt_price: float
  picnic_price: float
  rib_price: float
  ham_price: float
  belly_price: float

# Type alias to represent a row in a sqlite3 table of purchase records
Row = Tuple[str, float, float, float, float, float, float, float, float, float]

def from_cursor(row: Row) -> CutoutRecord:
  """ Creates a new CutoutRecord out of a Row fetched from a sqlite3 table """
  (date, primal_loads, trimming_loads,
      carcass_price, loin_price, butt_price, picnic_price, rib_price, ham_price, belly_price) = row

  return CutoutRecord(
    date = datetime.strptime("%Y-%m-%d", date),
    primal_loads = primal_loads,
    trimming_loads = trimming_loads,
    carcass_price = carcass_price,
    loin_price = loin_price,
    butt_price = butt_price,
    picnic_price = picnic_price,
    rib_price = rib_price,
    ham_price = ham_price,
    belly_price = belly_price)

def parse_line(loads: List[str], cutout: List[str]) -> CutoutRecord:
  """ Parses lines read from a Daily Pork Report csv file into a CutoutRecord """
  (loads_date, primal_loads, trimming_loads) = loads
  (cutout_date, carcass_price, loin_price, butt_price, picnic_price, rib_price, ham_price, belly_price) = cutout

  assert loads_date == cutout_date

  return CutoutRecord(
    date = datetime.strptime(cutout_date, "%m/%d/%Y"),
    primal_loads = float(primal_loads),
    trimming_loads = float(trimming_loads),
    carcass_price = float(carcass_price),
    loin_price = float(loin_price),
    butt_price = float(butt_price),
    picnic_price = float(picnic_price),
    rib_price = float(rib_price),
    ham_price = float(ham_price),
    belly_price = float(belly_price))
