from enum import Enum
from xml.etree.ElementTree import Element
from typing import Iterator, Tuple, Optional as Maybe
from datetime import date, datetime, timedelta

from .api import get_optional, fetch, filter_section, Report, Attributes
from .model.purchase import PurchaseRecord
from .model.purchase_type import PurchaseType, Seller, Arrangement, Basis

class Section(Enum):
  VOLUME = 'Current Volume by Purchase Type'
  BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
  CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
  CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
  AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
  SOWS = 'Sows'
  STATES = 'State of Origin'

# Lookup table for purchase type descriptions as declared in the HG200 report from the USDA
PURCHASE_TYPES = {
  'Negotiated (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.CARCASS),
  'Negotiated Formula (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),
  'Combined Negotiated/Negotiated Formula (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.ALL_NEGOTIATED, Basis.CARCASS),
  'Swine/Pork Market Formula (carcass basis)': PurchaseType(Seller.PRODUCER, Arrangement.MARKET_FORMULA, Basis.CARCASS),
  'Negotiated (live basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.LIVE),
  'Negotiated Formula (live basis)': PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.LIVE),
  'Combined Negotiated/Negotiated Formula (live basis)': PurchaseType(Seller.PRODUCER, Arrangement.ALL_NEGOTIATED, Basis.LIVE)
}

Line = Tuple[str, str, str, Maybe[str], Maybe[str], Maybe[str], Maybe[str], Maybe[str]]

def create_record(line: Line) -> PurchaseRecord:
  """ Creates a SlaughterRecord from values retreived from the daily Slaughtered Swine Report """
  (_, date, purchase_type, head_count, low_price, high_price, avg_price, _) = line

  (seller, arrangement, basis) = PURCHASE_TYPES[purchase_type]

  return PurchaseRecord(
    date = datetime.strptime(date, "%m/%d/%Y"),
    seller = seller,
    arrangement = arrangement,
    basis = basis,
    head_count = int(head_count.replace(',', '')) if head_count else 0,
    avg_price = float(avg_price) if avg_price else None,
    low_price = float(low_price) if low_price else None,
    high_price = float(high_price) if high_price else None)

def get_attributes(attr: Attributes) -> Line:
  return (
    attr['report_date'],
    attr['reported_for_date'],
    attr['purchase_type'],
    get_optional(attr, 'head_count'),
    get_optional(attr, 'price_low'),
    get_optional(attr, 'price_high'),
    get_optional(attr, 'wtd_avg'),
    get_optional(attr, 'rolling_avg'))

def from_attributes(attributes: Attributes) -> PurchaseRecord:
  return create_record(get_attributes(attributes))

def get_purchases(start_date: date, end_date: date=date.today()) -> Iterator[PurchaseRecord]:
  response = fetch(Report.PURCHASED_SWINE, start_date + timedelta(days=1), end_date)
  attributes = filter_section(response, Section.BARROWS_AND_GILTS.value)

  return map(from_attributes, attributes)
