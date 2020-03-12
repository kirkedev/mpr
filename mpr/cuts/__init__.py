from datetime import date
from typing import Iterator

from .cut_type import CutType
from .cut_type import cut_types
from .model import Cut
from .model import parse_record
from .report import lm_pk602
from ..data.repository import Repository


async def daily(start: date, end: date, *types: CutType) -> Iterator[Cut]:
    sections = (lm_pk602.Section(key) for key, value in cut_types.items() if value in types)
    data = await Repository(lm_pk602).query(start, min(lm_pk602.latest, end), *sections)
    return map(parse_record, data)
