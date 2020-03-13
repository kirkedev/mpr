from typing import Iterator
from typing import NamedTuple

from numpy import allclose
from numpy import dtype
from numpy import float32
from numpy import rec
from numpy import recarray
from numpy import uint32
from numpy import uint8

from .purchase_type import purchase_types
from ..data import Date
from ..data import Record
from ..data import date64
from ..data import date_ordinal
from ..data import get_optional
from ..data import opt_float
from ..data import opt_int
from ..data import parse_date
from ..data import unicode

date_format = "%m/%d/%Y"


class Purchase(NamedTuple):
    report: str
    date: Date
    report_date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    avg_price: float32
    low_price: float32
    high_price: float32

    def __hash__(self) -> int:
        return hash((self[0], *map(date_ordinal, self[1:3]), *self[3:6]))

    def __eq__(self, other) -> bool:
        return (isinstance(other, Purchase) and hash(self) == hash(other) and
            allclose(self[6:], other[6:], equal_nan=True))


def to_array(records: Iterator[Purchase]) -> recarray:
    return rec.array(list(records), dtype=dtype([
        ('report', unicode(8)),
        ('date', date64),
        ('report_date', date64),
        ('seller', uint8),
        ('arrangement', uint8),
        ('basis', uint8),
        ('head_count', uint32),
        ('avg_price', float32),
        ('low_price', float32),
        ('high_price', float32)
    ]))


def parse_record(record: Record) -> Purchase:
    report = record['slug'].lower()
    report_date = record['report_date']
    record_date = get_optional(record, 'reported_for_date') or report_date

    purchase_type = record['purchase_type']
    (seller, arrangement, basis) = purchase_types[purchase_type]

    return Purchase(
        report=report,
        date=parse_date(record_date, date_format),
        report_date=parse_date(report_date, date_format),
        seller=seller.value,
        arrangement=arrangement.value,
        basis=basis.value,
        head_count=opt_int(record, 'head_count'),
        avg_price=opt_float(record, 'wtd_avg'),
        low_price=opt_float(record, 'price_low'),
        high_price=opt_float(record, 'price_high'))
