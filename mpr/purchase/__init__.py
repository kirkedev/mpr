from datetime import date
from typing import Iterator

from .model import Purchase
from .model import parse_record
from .report import lm_hg200
from ..data.repository import Repository


async def daily(start: date, end: date) -> Iterator[Purchase]:
    end = min(lm_hg200.latest, end)
    print(lm_hg200.latest)
    purchases = await Repository(lm_hg200).query(start, end, lm_hg200.Section.BARROWS_AND_GILTS)
    return map(parse_record, purchases)
