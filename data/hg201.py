from enum import Enum
from xml.etree.ElementTree import Element
from typing import Iterator, Tuple, Optional as Maybe
from datetime import date, datetime, timedelta

from .api import get_optional, fetch, filter_section, Report, Attributes
from .model.slaughter import SlaughterRecord
from .model.purchase_type import PurchaseType, Seller, Arrangement, Basis

class Section(Enum):
  SUMMARY = 'Summary'
  BARROWS_AND_GILTS = 'Barrows/Gilts'
  CARCASS_MEASUREMENTS = 'Carcass Measurements'
  SOWS_AND_BOARS = 'Sows/Boars'
  SCHEDULED_SWINE = '14-Day Scheduled Swine'
  NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'

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

def create_record(line: Line) -> SlaughterRecord:
  """ Creates a SlaughterRecord from values retreived from the daily Slaughtered Swine Report """
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

def get_attributes(attr: Attributes) -> Line:
  return (
    attr['report_date'],
    attr['for_date_begin'],
    attr['purchase_type'],
    get_optional(attr, 'head_count'),
    get_optional(attr, 'base_price'),
    get_optional(attr, 'avg_net_price'),
    get_optional(attr, 'lowest_net_price'),
    get_optional(attr, 'highest_net_price'),
    get_optional(attr, 'avg_live_weight'),
    get_optional(attr, 'avg_carcass_weight'),
    get_optional(attr, 'avg_sort_loss'),
    get_optional(attr, 'avg_backfat'),
    get_optional(attr, 'avg_loin_depth'),
    get_optional(attr, 'loineye_area'),
    get_optional(attr, 'avg_lean_percent'))

def create_records(attributes: Attributes) -> SlaughterRecord:
  return create_record(get_attributes(attributes))

def get_slaughter(start_date: date, end_date: date=date.today()) -> Iterator[SlaughterRecord]:
  response = fetch(Report.SLAUGHTERED_SWINE, start_date + timedelta(days=1), end_date)
  attributes = filter_section(response, Section.BARROWS_AND_GILTS.value)

  return map(create_records, attributes)
