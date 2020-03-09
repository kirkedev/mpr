from typing import Dict
from typing import Iterator
from datetime import date

from ..purchase_type import PurchaseType, Seller, Arrangement, Basis
from ..report import PurchaseReport
from ..data import parse_date
from ..data import get_optional
from ..data import opt_int
from ..data import opt_float
from ..data import Record
from ..data.repository import Repository

from .model import Purchase

date_format = "%m/%d/%Y"


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


def parse_record(record: Record) -> Purchase:
    report_date_string = record['report_date']
    record_date_string = get_optional(record, 'reported_for_date') or report_date_string

    purchase_type = record['purchase_type']
    (seller, arrangement, basis) = purchase_types[purchase_type]

    return Purchase(
        report=record['slug'].lower(),
        date=parse_date(record_date_string, date_format),
        report_date=parse_date(report_date_string, date_format),
        seller=seller.value,
        arrangement=arrangement.value,
        basis=basis.value,
        head_count=opt_int(record, 'head_count'),
        avg_price=opt_float(record, 'wtd_avg'),
        low_price=opt_float(record, 'price_low'),
        high_price=opt_float(record, 'price_high'))


async def fetch_purchase(report: PurchaseReport, start: date, end=date.today()) -> Iterator[Purchase]:
    purchases = await Repository(report).query(start, end, report.Section.BARROWS_AND_GILTS)
    return map(parse_record, purchases)
