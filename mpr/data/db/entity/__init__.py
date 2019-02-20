from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar
from typing import Tuple
from typing import Dict
from typing import Iterator

from tables import Atom
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
    def schema() -> Dict[str, Atom]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_row(cls, row: Row) -> Record:
        raise NotImplementedError

    @classmethod
    def get(cls) -> Iterator[Record]:
        return map(cls.from_row, cls.table.iterrows())

    @classmethod
    def query(cls, condition: str, params: Dict) -> Iterator[Record]:
        return map(cls.from_row, cls.table.where(condition, params))

    @classmethod
    def insert(cls, records: Iterator[Record]):
        for record in records:
            record.append()

        cls.commit()

    @classmethod
    def commit(cls):
        cls.table.flush()

    @classmethod
    @abstractmethod
    def append(cls, record: Record):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def append_rows(cls, records: Iterator[Record]):
        raise NotImplementedError
