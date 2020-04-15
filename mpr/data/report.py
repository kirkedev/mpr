from abc import ABC
from abc import abstractmethod
from datetime import date
from datetime import timedelta
from enum import Enum
from typing import Tuple
from typing import TypeVar

from dateutil.relativedelta import relativedelta
from isoweek import Week

from . import chicago_time

Record = TypeVar('Record', bound=Tuple)


class Section(str, Enum):
    def __str__(self):
        return self.value


class Report(ABC):
    slug: str
    description: str
    hour: int

    def __init__(self, slug: str, description: str, hour: int):
        self.slug = slug
        self.description = description
        self.hour = hour

    def __str__(self):
        return self.slug

    @property
    @abstractmethod
    def latest(self) -> date:
        raise NotImplementedError


class DailyReport(Report):
    @property
    def latest(self) -> date:
        now = chicago_time()
        weekday = now.weekday()

        if weekday > 4:
            return now - timedelta(days=weekday - 4)

        latest = now if now > chicago_time(self.hour) else now - timedelta(days=1)
        return latest.date()


class WeeklyReport(Report):
    weekday: int

    def __init__(self, slug: str, description: str, weekday: int, hour: int):
        Report.__init__(self, slug, description, hour)
        self.weekday = weekday

    @property
    def latest(self) -> date:
        now = chicago_time()
        release_date = Week.withdate(now.date()).day(self.weekday)
        release = chicago_time(self.hour).replace(release_date.year, release_date.month, release_date.day)
        latest = release if now > release else release - relativedelta(weeks=1)

        return latest.date()
