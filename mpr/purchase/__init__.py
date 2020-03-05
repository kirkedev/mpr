from datetime import date
from typing import Iterator

from ..report import lm_hg200
from ..report import lm_hg202
from ..report import lm_hg203

from .api import fetch_purchase
from .model import Purchase


async def prior_day(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(lm_hg200, start, end)


async def morning(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(lm_hg202, start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(lm_hg203, start, end)
