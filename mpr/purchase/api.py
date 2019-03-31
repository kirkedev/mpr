from typing import Dict
from typing import Iterator
from enum import Enum
from datetime import timedelta
from datetime import date

from ..api import Attributes
from ..api import Report
from ..api import get_optional
from ..api import opt_int
from ..api import opt_float
from ..api import fetch
from ..api import filter_section
from ..date import from_string
from ..purchase_type import PurchaseType, Seller, Arrangement, Basis

from .model import Purchase

date_format = "%m/%d/%Y"


class Section(Enum):
    # VOLUME = 'Current Volume by Purchase Type'
    BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
    # CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
    # CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
    # AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
    # SOWS = 'Sows'
    # STATES = 'State of Origin'


purchase_types: Dict[str, PurchaseType] = {
    'Negotiated (carcass basis)':
        (Seller.ALL, Arrangement.NEGOTIATED, Basis.CARCASS),

    'Negotiated Formula (carcass basis)':
        (Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),

    'Swine/Pork Market Formula (carcass basis)':
        (Seller.ALL, Arrangement.MARKET_FORMULA, Basis.CARCASS),

    'Negotiated (live basis)':
        (Seller.ALL, Arrangement.NEGOTIATED, Basis.LIVE),

    'Negotiated Formula (live basis)':
        (Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.LIVE),

    'Combined Negotiated/Negotiated Formula (carcass basis)':
        (Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.CARCASS),

    'Combined Negotiated/Negotiated Formula (live basis)':
        (Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.LIVE)
}


def parse_attributes(attr: Attributes) -> Purchase:
    report_date_string = attr['report_date']
    record_date_string = get_optional(attr, 'reported_for_date') or report_date_string

    purchase_type = attr['purchase_type']
    (seller, arrangement, basis) = purchase_types[purchase_type]

    return Purchase(
        date=from_string(record_date_string, date_format),
        report_date=from_string(report_date_string, date_format),
        seller=seller.value,
        arrangement=arrangement.value,
        basis=basis.value,
        head_count=opt_int(attr, 'head_count'),
        avg_price=opt_float(attr, 'wtd_avg'),
        low_price=opt_float(attr, 'price_low'),
        high_price=opt_float(attr, 'price_high'))


async def fetch_purchase(report: Report, start: date, end=date.today()) -> Iterator[Purchase]:
    response = await fetch(report, start, end)
    return map(parse_attributes, filter_section(response, Section.BARROWS_AND_GILTS.value))


async def prior_day(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(Report.PURCHASED_SWINE, start + timedelta(days=1), end)


async def morning(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(Report.DIRECT_HOG_MORNING, start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(Report.DIRECT_HOG_AFTERNOON, start, end)


lm_hg200 = hg200 = prior_day
lm_hg202 = hg202 = morning
lm_hg203 = hg203 = afternoon
