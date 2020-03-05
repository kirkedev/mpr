from typing import Dict
from typing import Optional

from numpy import float32
from numpy import nan
from numpy import uint32

Attributes = Dict[str, str]


def strip_commas(value: str) -> str:
    return value.replace(',', '')


def get_optional(attr: Attributes, key: str) -> Optional[str]:
    return attr[key] if key in attr and attr[key] != 'null' else None


def opt_float(attr: Attributes, key: str) -> float32:
    value = get_optional(attr, key)
    return float32(strip_commas(value)) if value else nan


def opt_int(attr: Attributes, key: str) -> uint32:
    value = get_optional(attr, key)
    return uint32(strip_commas(value)) if value else 0
