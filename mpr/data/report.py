from abc import ABC
from abc import abstractmethod
from datetime import date
from datetime import timedelta
from enum import Enum
from typing import Tuple
from typing import TypeVar

from dateutil import utils
from dateutil.relativedelta import relativedelta
from dateutil.tz import gettz
from isoweek import Week

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
        today = utils.today(gettz('America/Chicago'))
        weekday = today.weekday()

        if weekday > 4:
            return today - timedelta(days=weekday - 4)

        release = today.replace(hour=self.hour, minute=0, second=0, microsecond=0)
        return today.date() if today > release else (today - timedelta(days=1)).date()


class WeeklyReport(Report):
    weekday: int

    def __init__(self, slug: str, description: str, weekday: int, hour: int):
        Report.__init__(self, slug, description, hour)
        self.weekday = weekday

    @property
    def latest(self) -> date:
        today = utils.today(gettz('America/Chicago'))
        release = today.replace(hour=self.hour, minute=0, second=0, microsecond=0)

        return Week.withdate(today).day(self.weekday) if today > release else \
            (today - relativedelta(weeks=1, weekday=self.weekday)).date()
