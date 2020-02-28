from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import NamedTuple
from typing import TypeVar
from typing import Tuple

from numpy import dtype

Record = TypeVar('Record', bound=NamedTuple)


class Entity(Generic[Record], ABC):
    @property
    @abstractmethod
    def schema(self) -> dtype:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_row(row: Tuple) -> Record:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def to_row(record: Record) -> Tuple:
        raise NotImplementedError
