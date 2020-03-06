from datetime import date
from datetime import timedelta

from typing import Iterator

from ..report import lm_hg201
from .api import fetch_slaughter
from .model import Slaughter


async def get_slaughter(start: date, end=date.today()) -> Iterator[Slaughter]:
    if not lm_hg201.released(end):
        end -= timedelta(days=1)

    return await fetch_slaughter(start, end)
