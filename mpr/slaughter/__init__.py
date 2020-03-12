from datetime import date
from typing import Iterator

from .model import Slaughter
from .model import parse_record
from .report import lm_hg201
from ..data.repository import Repository


async def daily(start: date, end: date) -> Iterator[Slaughter]:
    end = min(lm_hg201.latest, end)
    slaughter = await Repository(lm_hg201).query(start, end, lm_hg201.Section.BARROWS_AND_GILTS)
    return map(parse_record, slaughter)
