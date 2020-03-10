from typing import Dict
from typing import Iterator
from datetime import date

from .cut_type import CutType
from .model import Cut
from ..data import opt_float
from ..data import opt_int
from ..data import parse_date
from ..data import Record
from ..data.repository import Repository
from ..report import CutoutReport
from ..report import Section

date_format = "%m/%d/%Y"

cut_types: Dict[str, CutType] = {
    'Loin Cuts': CutType.LOIN,
    'Butt Cuts': CutType.BUTT,
    'Picnic Cuts': CutType.PICNIC,
    'Ham Cuts': CutType.HAM,
    'Belly Cuts': CutType.BELLY,
    'Sparerib Cuts': CutType.RIB,
    'Jowl Cuts': CutType.JOWL,
    'Trim Cuts': CutType.TRIM,
    'Variety Cuts': CutType.VARIETY,
    'Added Ingredient Cuts': CutType.ADDED_INGREDIENT
}


def parse_record(record: Record) -> Cut:
    report = record['slug'].lower()
    report_date = parse_date(record['report_date'], date_format)
    section = record['label']

    return Cut(
        report=report,
        date=report_date,
        report_date=report_date,
        type=cut_types[section],
        description=record['Item_Description'],
        weight=opt_int(record, 'total_pounds'),
        avg_price=opt_float(record, 'weighted_average'),
        low_price=opt_float(record, 'price_range_low'),
        high_price=opt_float(record, 'price_range_high'))


async def fetch_cuts(report: CutoutReport, cut: CutType, start: date, end=date.today()) -> Iterator[Cut]:
    cuts = await Repository(report).query(start, end, Section(cut.name))
    return map(parse_record, cuts)
