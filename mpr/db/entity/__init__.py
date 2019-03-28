from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar
from typing import Tuple
from typing import Dict
from typing import Iterator

from numpy import dtype
from tables import Table
from tables.tableextension import Row

Record = TypeVar('Record', bound=Tuple)


class Entity(Generic[Record], ABC):
    @staticmethod
    @property
    @abstractmethod
    def table() -> Table:
        raise NotImplementedError

    @staticmethod
    @property
    @abstractmethod
    def schema() -> dtype:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_row(row: Row) -> Record:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def to_row(record: Record) -> Tuple:
        raise NotImplementedError

    @classmethod
    def get(cls) -> Iterator[Record]:
        return map(cls.from_row, cls.table.iterrows())

    @classmethod
    def query(cls, condition: str, params: Dict) -> Iterator[Record]:
        return map(cls.from_row, cls.table.where(condition, params))

    @classmethod
    def insert(cls, records: Iterator[Record]):
        existing = set(map(hash, cls.get()))
        new = filter(lambda it: hash(it) not in existing, records)
        rows = list(map(cls.to_row, new))

        if len(rows) > 0:
            cls.table.append(rows)
            cls.commit()

    @classmethod
    def commit(cls):
        cls.table.flush()
