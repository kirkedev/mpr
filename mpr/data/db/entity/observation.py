from abc import ABC
from typing import Iterator
from datetime import date

import numpy as np

from . import Entity
from . import Record


class Observation(Entity[Record], ABC):
    @classmethod
    def get(cls) -> Iterator[Record]:
        return map(cls.from_row, cls.table.itersorted(sortby='date'))

    @classmethod
    def get_date(cls, observation_date: date) -> Iterator[Record]:
        return super(Observation, cls).query("""date == observation_date""", {
            'observation_date': observation_date
        })

    @classmethod
    def get_range(cls, start: date, end=date.today()) -> Iterator[Record]:
        return super(Observation, cls).query("""(start <= date) & (date <= end)""", {
            'start': start.toordinal(),
            'end': end.toordinal()
        })

    @classmethod
    def get_recent(cls, days: int) -> Iterator[Record]:
        today = date.today()
        start = np.busday_offset(today, -days).astype('O')

        return cls.get_range(start, today)

    @classmethod
    def get_year(cls, year: int) -> Iterator[Record]:
        return cls.get_range(date(year, 1, 1), date(year, 12, 31))

    @classmethod
    def first(cls) -> Record:
        return cls.table[cls.table.colindexes['date'][0]]

    @classmethod
    def last(cls) -> Record:
        return cls.table[cls.table.colindexes['date'][-1]]

    @classmethod
    def dates(cls) -> Iterator[date]:
        return map(date.fromordinal, set(cls.table.cols.date[:]))
