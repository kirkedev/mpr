from xml.etree.ElementTree import Element
from typing import Iterator, Tuple, Optional as Maybe
from datetime import date, datetime, timedelta

from .api import get_optional, fetch, Report
from .model.slaughter import SlaughterRecord
from .model.purchase_type import PurchaseType, Seller, Arrangement, Basis

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

Line = Tuple[str, str, str, Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str],
    Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str]]

def parse(line: Line) -> SlaughterRecord:
  """ Parses a line read from the daily Slaughtered Swine Report into a SlaughterRecord """
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

def parse_element(element: Element) -> Tuple[str, Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str],
    Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str]]:

  attr = element.attrib

  purchase_type = attr['purchase_type']
  head_count = get_optional(attr, 'head_count')
  base_price = get_optional(attr, 'base_price')
  net_price = get_optional(attr, 'avg_net_price')
  low_price = get_optional(attr, 'lowest_net_price')
  high_price = get_optional(attr, 'highest_net_price')
  live_weight = get_optional(attr, 'avg_live_weight')
  carcass_weight = get_optional(attr, 'avg_carcass_weight')
  sort_loss = get_optional(attr, 'avg_sort_loss')
  backfat = get_optional(attr, 'avg_backfat')
  loin_depth = get_optional(attr, 'avg_loin_depth')
  loineye_area = get_optional(attr, 'loineye_area')
  lean_percent = get_optional(attr, 'avg_lean_percent')

  return (purchase_type, head_count, base_price, net_price, low_price, high_price, live_weight,
      carcass_weight, sort_loss, backfat, loin_depth, loineye_area, lean_percent)

def generate_slaughter(reports: Iterator[Tuple[str, Element]]) -> Iterator[SlaughterRecord]:
  depth = 0
  report = None

  for event, element in reports:
    if element.tag == 'report':
      report = element.attrib.get('label')

    if element.tag == 'record':
      if event == 'start':
        if depth == 0:
          report_date = element.attrib['report_date']
          for_date = element.attrib['for_date_begin']

        if depth == 1 and report == 'Barrows/Gilts':
          yield parse((report_date, for_date, *parse_element(element)))

        depth += 1

      if event == 'end':
        depth -= 1

        if depth == 0:
          report = None

def get_slaughter(start_date: date, end_date: date=date.today()) -> Iterator[SlaughterRecord]:
  elements = fetch(Report.SLAUGHTERED_SWINE, start_date + timedelta(days=1), end_date)

  #skip top-level results metadata
  next(elements, None)

  #skip top-level report metadata
  next(elements, None)

  return generate_slaughter(elements)
