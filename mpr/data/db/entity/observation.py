from abc import ABC
from typing import Iterator
from datetime import date

from . import Entity
from . import Record


class Observation(Entity[Record], ABC):
    @classmethod
    def get(cls) -> Iterator[Record]:
        return map(cls.from_row, cls.table.itersorted(sortby='date'))

    @classmethod
    def get_date(cls, observation_date: date) -> Iterator[Record]:
        return super(Observation, cls).query("""date == observation_date""", {
            'observation_date': observation_date.toordinal()
        })

    @classmethod
    def get_range(cls, start: date, end=date.today()) -> Iterator[Record]:
        return super(Observation, cls).query("""(start <= date) & (date <= end)""", {
            'start': start.toordinal(),
            'end': end.toordinal()
        })

    @classmethod
    def dates(cls) -> Iterator[date]:
        return map(date.fromordinal, set(cls.table.cols.date[:]))
