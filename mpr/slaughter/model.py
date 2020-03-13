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
from ..data import opt_float
from ..data import opt_int
from ..data import parse_date
from ..data import unicode

date_format = "%m/%d/%Y"


class Slaughter(NamedTuple):
    report: str
    date: Date
    report_date: Date
    seller: uint8
    arrangement: uint8
    basis: uint8
    head_count: uint32
    base_price: float32
    net_price: float32
    low_price: float32
    high_price: float32
    live_weight: float32
    carcass_weight: float32
    sort_loss: float32
    backfat: float32
    loin_depth: float32
    loineye_area: float32
    lean_percent: float32

    def __hash__(self) -> int:
        return hash((self[0], *map(date_ordinal, self[1:3]), self[3:6]))

    def __eq__(self, other) -> bool:
        return (isinstance(other, Slaughter) and hash(self) == hash(other) and
            allclose(self[6:], other[6:], equal_nan=True))

    @property
    def total_weight(self) -> float:
        return self.head_count * self.carcass_weight

    @property
    def total_value(self) -> float:
        return self.total_weight * self.net_price

    @property
    def avg_price(self) -> float:
        return self.total_value / self.total_weight


def parse_record(record: Record) -> Slaughter:
    purchase_type = record['purchase_type']
    (seller, arrangement, basis) = purchase_types[purchase_type]

    return Slaughter(
        report=record['slug'].lower(),
        date=parse_date(record['for_date_begin'], date_format),
        report_date=parse_date(record['report_date'], date_format),
        seller=seller.value,
        arrangement=arrangement.value,
        basis=basis.value,
        head_count=opt_int(record, 'head_count'),
        base_price=opt_float(record, 'base_price'),
        net_price=opt_float(record, 'avg_net_price'),
        low_price=opt_float(record, 'lowest_net_price'),
        high_price=opt_float(record, 'highest_net_price'),
        live_weight=opt_float(record, 'avg_live_weight'),
        carcass_weight=opt_float(record, 'avg_carcass_weight'),
        sort_loss=opt_float(record, 'avg_sort_loss'),
        backfat=opt_float(record, 'avg_backfat'),
        loin_depth=opt_float(record, 'avg_loin_depth'),
        loineye_area=opt_float(record, 'loineye_area'),
        lean_percent=opt_float(record, 'avg_lean_percent'))


def to_array(records: Iterator[Slaughter]) -> recarray:
    return rec.array(list(records), dtype=dtype([
        ('report', unicode(8)),
        ('date', date64),
        ('report_date', date64),
        ('seller', uint8),
        ('arrangement', uint8),
        ('basis', uint8),
        ('head_count', uint32),
        ('base_price', float32),
        ('net_price', float32),
        ('low_price', float32),
        ('high_price', float32),
        ('live_weight', float32),
        ('carcass_weight', float32),
        ('sort_loss', float32),
        ('backfat', float32),
        ('loin_depth', float32),
        ('loineye_area', float32),
        ('lean_percent', float32)
    ]))
