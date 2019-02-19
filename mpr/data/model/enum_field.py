from typing import List
from enum import Enum
from enum import unique


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
