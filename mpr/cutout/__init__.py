from datetime import date
from itertools import starmap
from typing import Iterator

from .model import Cutout
from .model import parse_record
from .report import lm_pk602
from ..data.repository import Repository


async def afternoon(start: date, end: date) -> Iterator[Cutout]:
    end = min(lm_pk602.latest, end)
    cutout, volume = await Repository(lm_pk602).query(start, end, lm_pk602.Section.CUTOUT, lm_pk602.Section.VOLUME)
    return starmap(parse_record, zip(cutout, volume))
