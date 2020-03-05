from typing import Dict
from typing import Optional

from numpy import float32
from numpy import nan
from numpy import uint32

Record = Dict[str, str]


def strip_commas(value: str) -> str:
    return value.replace(',', '')


def get_optional(record: Record, key: str) -> Optional[str]:
    return record[key] if key in record and record[key] != 'null' else None


def opt_float(record: Record, key: str) -> float32:
    value = get_optional(record, key)
    return float32(strip_commas(value)) if value else nan


def opt_int(record: Record, key: str) -> uint32:
    value = get_optional(record, key)
    return uint32(strip_commas(value)) if value else 0
