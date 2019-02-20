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
date_type = dtype('datetime64[D]')
Date = type(date_type)


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
