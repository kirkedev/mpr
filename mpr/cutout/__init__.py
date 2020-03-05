from datetime import date
from typing import Iterator

from ..report import lm_pk600
from ..report import lm_pk602

from .api import fetch_cutout
from .model import Cutout


async def morning(start: date, end=date.today()) -> Iterator[Cutout]:
    return await fetch_cutout(lm_pk600, start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Cutout]:
    return await fetch_cutout(lm_pk602, start, end)
