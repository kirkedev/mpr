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

    @classmethod
    @abstractmethod
    def from_row(cls, row: Row) -> Record:
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
    @abstractmethod
    def insert(cls, records: Iterator[Record]):
        cls.table.append(list(map(cls.to_row, records)))
        cls.commit()

    @classmethod
    def commit(cls):
        cls.table.flush()
