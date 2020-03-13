from typing import Iterator
from typing import NamedTuple

from numpy import allclose
from numpy import dtype
from numpy import float32
from numpy import rec
from numpy import recarray

from ..data import Date
from ..data import Record
from ..data import date64
from ..data import date_ordinal
from ..data import parse_date
from ..data import unicode

date_format = "%m/%d/%Y"


class Cutout(NamedTuple):
    report: str
    date: Date
    report_date: Date
    primal_loads: float32
    trimming_loads: float32
    carcass_price: float32
    loin_price: float32
    butt_price: float32
    picnic_price: float32
    rib_price: float32
    ham_price: float32
    belly_price: float32

    def __hash__(self) -> int:
        return hash((self[0], *map(date_ordinal, self[1:3])))

    def __eq__(self, other) -> bool:
        return (isinstance(other, Cutout) and hash(self) == hash(other) and
            allclose(self[3:], other[3:], equal_nan=True))

    @property
    def loads(self) -> int:
        return self.primal_loads + self.trimming_loads

    @property
    def value(self) -> float:
        return self.loads * self.carcass_price


def parse_record(cutout: Record, volume: Record) -> Cutout:
    report = cutout['slug'].lower()
    report_date = parse_date(cutout['report_date'], date_format)

    return Cutout(
        report=report,
        date=report_date,
        report_date=report_date,
        primal_loads=float32(volume['temp_cuts_total_load']),
        trimming_loads=float32(volume['temp_process_total_load']),
        carcass_price=float32(cutout['pork_carcass']),
        loin_price=float32(cutout['pork_loin']),
        butt_price=float32(cutout['pork_butt']),
        picnic_price=float32(cutout['pork_picnic']),
        rib_price=float32(cutout['pork_rib']),
        ham_price=float32(cutout['pork_ham']),
        belly_price=float32(cutout['pork_belly']))


def to_array(records: Iterator[Cutout]) -> recarray:
    return rec.array(list(records), dtype=dtype([
        ('report', unicode(8)),
        ('date', date64),
        ('report_date', date64),
        ('primal_loads', float32),
        ('trimming_loads', float32),
        ('carcass_price', float32),
        ('loin_price', float32),
        ('butt_price', float32),
        ('picnic_price', float32),
        ('rib_price', float32),
        ('ham_price', float32),
        ('belly_price', float32)
    ]))
