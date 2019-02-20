from abc import ABC
from abc import abstractmethod
from typing import TypeVar
from typing import Optional
from typing import Dict
from typing import Iterator

from numpy import dtype
from numpy import uint32
from numpy import float32
from numpy import nan

from tables import Atom
from tables import Table
from tables.tableextension import Row

T = TypeVar('T')
Attributes = Dict[str, str]
Date = type(dtype('datetime64[D]'))


def get_optional(attr: Attributes, key: str) -> Optional[T]:
    return attr[key] if key in attr and attr[key] != 'null' else None


def opt_float(attr: Attributes, key: str) -> float32:
    value = get_optional(attr, key)
    return float(value.replace(',', '')) if value else nan


def opt_int(attr: Attributes, key: str) -> uint32:
    value = get_optional(attr, key)
    return int(value.replace(',', '')) if value else nan


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
    @abstractmethod
    def from_row(cls, row: Row) -> 'Model':
        raise NotImplementedError

    @classmethod
    def get(cls) -> 'Iterator[Model]':
        return map(cls.from_row, cls.table.iterrows())

    @classmethod
    def query(cls, condition: str, params: Dict) -> 'Iterator[Model]':
        return map(cls.from_row, cls.table.where(condition, params))

    @classmethod
    def insert(cls, records: 'Iterator[Model]'):
        for record in records:
            record.append()

        cls.commit()

    @classmethod
    def commit(cls):
        cls.table.flush()

    @abstractmethod
    def append(self):
        raise NotImplementedError

    def save(self):
        self.append()
        self.commit()
