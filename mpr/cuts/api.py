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
    cut_type = cut_types[section].value
    description = record['Item_Description']

    return Cut(
        report=report,
        date=report_date,
        report_date=report_date,
        type=cut_type,
        description=description,
        weight=opt_int(record, 'total_pounds'),
        avg_price=opt_float(record, 'weighted_average'),
        low_price=opt_float(record, 'price_range_low'),
        high_price=opt_float(record, 'price_range_high'))


async def fetch_cuts(report: CutoutReport, cut: CutType, start: date, end=date.today()) -> Iterator[Cut]:
    section = next(CutoutReport.Section(key) for key, value in cut_types.items() if value == cut)
    cuts = await Repository(report).query(start, end, section)
    return map(parse_record, cuts)
