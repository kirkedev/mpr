from typing import TypeVar
from typing import Dict

from numpy import dtype

T = TypeVar('T')
Attributes = Dict[str, str]

date_type = dtype('datetime64[D]')
Date = type(date_type)
