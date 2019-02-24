from typing import Iterator

from mpr.data.model.slaughter import Slaughter
from mpr.data.model.purchase_type import Arrangement


total_weight = lambda head_count, weight: head_count * weight
total_value = lambda weight, price: weight * price
weighted_price = lambda value, weight: value / weight


def filter_types(records: Iterator[Slaughter]) -> Iterator[Slaughter]:
    return filter(lambda it: it.arrangement in (
        Arrangement.NEGOTIATED,
        Arrangement.MARKET_FORMULA,
        Arrangement.NEGOTIATED_FORMULA
    ), records)
