from datetime import date
from typing import Iterator

from ..db import lm_hg200
from ..db import lm_hg202
from ..db import lm_hg203
from ..reports import PurchaseReport
from .api import fetch_purchase
from .model import Purchase


async def prior_day(start: date, end=date.today()) -> Iterator[Purchase]:
    records = await fetch_purchase(PurchaseReport.LM_HG200, start, end)
    lm_hg200.barrows_gilts.insert(records)
    return lm_hg200.barrows_gilts.get_range(start, end)


async def morning(start: date, end=date.today()) -> Iterator[Purchase]:
    records = await fetch_purchase(PurchaseReport.LM_HG202, start, end)
    lm_hg202.barrows_gilts.insert(records)
    return lm_hg202.barrows_gilts.get_range(start, end)


async def afternoon(start: date, end=date.today()) -> Iterator[Purchase]:
    records = await fetch_purchase(PurchaseReport.LM_HG203, start, end)
    lm_hg203.barrows_gilts.insert(records)
    return lm_hg203.barrows_gilts.get_range(start, end)
