from typing import TypeVar
from typing import Optional
from typing import List
from typing import Dict
from enum import Enum
from enum import unique

from numpy import dtype
from numpy import uint32
from numpy import float32
from numpy import nan

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


@unique
class EnumField(Enum):
    @classmethod
    def values(cls) -> List[Enum]:
        return list(map(lambda it: it.value, cls))

    def to_ordinal(self) -> int:
        return self.values().index(self.value)

    @classmethod
    def from_ordinal(cls, ordinal: int) -> 'EnumField':
        return list(cls)[ordinal]
