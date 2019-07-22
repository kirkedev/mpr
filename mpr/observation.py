from abc import ABC
from typing import Iterator
from datetime import date

from .entity import Entity
from .entity import Record


class Observation(Entity[Record], ABC):
    def get(self) -> Iterator[Record]:
        return map(self.from_row, self.table.itersorted(sortby='date'))

    def get_date(self, observation_date: date) -> Iterator[Record]:
        return super(Observation, self).query("""date == observation_date""", {
            'observation_date': observation_date.toordinal()
        })

    def get_range(self, start: date, end=date.today()) -> Iterator[Record]:
        return super(Observation, self).query("""(start <= date) & (date <= end)""", {
            'start': start.toordinal(),
            'end': end.toordinal()
        })

    def report_dates(self) -> Iterator[date]:
        return map(date.fromordinal, set(self.table.cols.report_date[:]))
