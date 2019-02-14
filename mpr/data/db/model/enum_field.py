from typing import Generic
from typing import TypeVar
from typing import List
from enum import Enum
from enum import unique

T = TypeVar('T', bound=EnumField)


@unique
class EnumField(Generic[T], Enum):
    @classmethod
    @property
    def values(cls) -> List[T]:
        return list(cls)

    def to_ordinal(self) -> int:
        return self.values.index(self)

    def from_ordinal(self, ordinal: int) -> T:
        return self.values[ordinal]
