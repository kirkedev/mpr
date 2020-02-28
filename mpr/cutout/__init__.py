from datetime import date
from typing import Iterator

from ..reports import CutoutReport
from .api import fetch_cutout
from .model import Cutout


async def morning(start: date, end=date.today()) -> Iterator[Cutout]:
    return await fetch_cutout(CutoutReport.LM_PK600, start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Cutout]:
    return await fetch_cutout(CutoutReport.LM_PK602, start, end)
