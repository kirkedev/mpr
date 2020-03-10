from datetime import date
from datetime import timedelta
from typing import Iterator

from .cut_type import CutType
from ..report import lm_pk600
from ..report import lm_pk602

from .api import fetch_cuts
from .model import Cut


async def daily(cut: CutType, start: date, end=date.today()) -> Iterator[Cut]:
    if not lm_pk600.has(end):
        end -= timedelta(days=1)

    return await fetch_cuts(lm_pk602, cut, start, end)
