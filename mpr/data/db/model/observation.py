from abc import ABC
from typing import Type
from typing import TypeVar
from typing import Tuple
from typing import Iterator
from datetime import date
from . import Model

T = TypeVar('T', bound=Observation)


class Observation(Model, ABC):
    @classmethod
    def get(cls: Type[T]) -> Iterator[T]:
        return map(cls.from_row, cls.table.itersorted())

    @classmethod
    def get_date(cls: Type[T], observation_date: date) -> Iterator[T]:
        return super(Observation, cls).query("""date == observation_date""", {
            'observation_date': observation_date
        })

    @classmethod
    def get_range(cls: Type[T], start: date, end=date.today()) -> Iterator[T]:
        return super(Observation, cls).query("""(start <= date) & (date <= end)""", {
            'start': start.toordinal(),
            'end': end.toordinal()
        })

    @classmethod
    def get_recent(cls: Type[T], days: int) -> Iterator[T]:
        today = date.today()
        start = np.busday_offset(today, -days).astype('O')

        return cls.get_range(start, today)

    @classmethod
    def get_year(cls: Type[T], year: int) -> Iterator[T]:
        return cls.get_range(date(year, 1, 1), date(year, 12, 31))

    @classmethod
    def first(cls: Type[T]) -> T:
        return cls.table[cls.table.colindexes['date'][0]]

    @classmethod
    def last(cls: Type[T]) -> T:
        return cls.table[cls.table.colindexes['date'][-1]]

    @classmethod
    def dates(cls: Type[T]) -> Iterator[date]:
        return map(date.fromordinal, set(cls.table.cols.date[:]))

    @classmethod
    def extent(cls: Type[T]) -> Tuple[date, date]:
        table = cls.table()
        date_column = table.cols.date
        date_index = table.colindexes['date']

        first = date.fromordinal(date_column[date_index[0]])
        last = date.fromordinal(date_column[date_index[-1]])

        return first, last
