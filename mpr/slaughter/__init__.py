from datetime import date
from typing import Iterator

from .api import fetch_slaughter
from .model import Slaughter


async def get_slaughter(start: date, end=date.today()) -> Iterator[Slaughter]:
    return await fetch_slaughter(start, end)
