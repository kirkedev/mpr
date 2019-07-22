from datetime import date
from typing import Iterator

from ..db import lm_pk600
from ..db import lm_pk602
from ..reports import CutoutReport
from .api import fetch_cutout
from .model import Cutout


async def morning(start: date, end=date.today()) -> Iterator[Cutout]:
    cutout = await fetch_cutout(CutoutReport.LM_PK600, start, end)
    lm_pk600.cutout.insert(cutout)
    return lm_pk600.cutout.get_range(start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Cutout]:
    cutout = await fetch_cutout(CutoutReport.LM_PK602, start, end)
    lm_pk602.cutout.insert(cutout)
    return lm_pk602.cutout.get_range(start, end)
