from datetime import date
from typing import Iterator

from .cut_type import CutType
from .cut_type import cut_types
from .model import Cut
from .model import parse_record
from .report import lm_pk602
from .report import lm_pk620
from ..data.repository import Repository


async def daily(start: date, end: date, *types: CutType) -> Iterator[Cut]:
    end = min(lm_pk602.latest, end)
    sections = (lm_pk602.Section(key) for key, value in cut_types.items() if value in types)
    data = await Repository(lm_pk602).query(start, end, *sections)
    return map(parse_record, data)


async def weekly(start: date, end: date, *types: CutType) -> Iterator[Cut]:
    latest = lm_pk620.latest
    start = min(latest, start)
    end = min(latest, end)

    sections = (lm_pk620.Section(key) for key, value in cut_types.items() if value in types)
    data = await Repository(lm_pk620).query(start, end, *sections)
    return map(parse_record, data)
