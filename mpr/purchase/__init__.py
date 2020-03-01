from datetime import date
from typing import Iterator

from ..report import PurchaseReport
from .api import fetch_purchase
from .model import Purchase


async def prior_day(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(PurchaseReport.LM_HG200, start, end)


async def morning(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(PurchaseReport.LM_HG202, start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Purchase]:
    return await fetch_purchase(PurchaseReport.LM_HG203, start, end)
