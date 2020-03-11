from abc import ABC
from datetime import date
from datetime import datetime
from enum import Enum
from typing import Generic
from typing import Iterator
from typing import NamedTuple
from typing import TypeVar

from pytz import timezone

Record = TypeVar('Record', bound=NamedTuple)


class Report(ABC, Generic[Record]):
    slug: str
    description: str
    hour: int

    def __init__(self, slug: str, description: str, hour: int):
        self.slug = slug
        self.description = description
        self.hour = hour

    def __str__(self):
        return self.slug

    def has(self, end: date) -> bool:
        now = datetime.now(tz=timezone('America/Chicago'))
        release = now.replace(end.year, end.month, end.day, self.hour, 0, 0, 0)
        return now > release

    async def fetch(self, start: date, end: date) -> Iterator[Record]:
        raise NotImplementedError


class Section(str, Enum):
    def __str__(self):
        return self.value
