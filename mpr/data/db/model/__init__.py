from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Iterator
from typing import Type
from typing import TypeVar

from tables import Atom
from tables import Table
from tables.tableextension import Row

T = TypeVar('T', bound=Model)


class Model(ABC):
    @staticmethod
    @property
    @abstractmethod
    def table() -> Table:
        raise NotImplementedError

    @staticmethod
    @property
    @abstractmethod
    def schema() -> Dict[str, Atom]:
        raise NotImplementedError

    @classmethod
    def get(cls: Type[T]) -> Iterator[T]:
        return map(cls.from_row, cls.table.iterrows())

    @classmethod
    def query(cls: Type[T], condition: str, params: Dict) -> Iterator[T]:
        return map(cls.from_row, cls.table.where(condition, params))

    @classmethod
    def insert(cls: T, records: Iterator[T]):
        table = cls.table

        for record in records:
            record.append()

        table.flush()

    @classmethod
    @abstractmethod
    def from_row(cls: Type[T], row: Row) -> T:
        raise NotImplementedError

    @abstractmethod
    def append(self):
        raise NotImplementedError

    @classmethod
    def commit(cls):
        cls.table.flush()
