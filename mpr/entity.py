from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import NamedTuple
from typing import TypeVar
from typing import Tuple
from typing import Dict
from typing import Iterator

from numpy import dtype
from tables import Table
from tables.tableextension import Row

Record = TypeVar('Record', bound=NamedTuple)


class Entity(Generic[Record], ABC):
    @property
    @abstractmethod
    def table(self) -> Table:
        raise NotImplementedError

    @property
    @abstractmethod
    def schema(self) -> dtype:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_row(row: Row) -> Record:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def to_row(record: Record) -> Tuple:
        raise NotImplementedError

    def get(self) -> Iterator[Record]:
        return map(self.from_row, self.table.iterrows())

    def query(self, condition: str, params: Dict) -> Iterator[Record]:
        return map(self.from_row, self.table.where(condition, params))

    def insert(self, records: Iterator[Record]):
        existing = set(map(hash, self.get()))
        new = filter(lambda it: hash(it) not in existing, records)
        rows = list(map(self.to_row, new))

        if len(rows) > 0:
            self.table.append(rows)
            self.commit()

    def commit(self):
        self.table.flush()
