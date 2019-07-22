from datetime import date
from typing import Iterator

from ..db import lm_hg201
from .api import fetch_slaughter
from .model import Slaughter


async def get_slaughter(start: date, end=date.today()) -> Iterator[Slaughter]:
    records = await fetch_slaughter(start, end)
    lm_hg201.barrows_gilts.insert(records)
    return lm_hg201.barrows_gilts.get_range(start, end)
