from enum import IntEnum
import numpy as np
from numpy import uint8

purchase_type = np.dtype([
    ('seller', uint8),
    ('arrangement', uint8),
    ('basis', uint8)
])

PurchaseType = type(purchase_type)


class Seller(IntEnum):
    ALL = 0
    PRODUCER = 1
    PACKER = 2


class Arrangement(IntEnum):
    ALL = 0
    NEGOTIATED = 1
    MARKET_FORMULA = 2
    NEGOTIATED_FORMULA = 3
    OTHER_MARKET_FORMULA = 4
    OTHER_PURCHASE = 5
    ALL_NEGOTIATED = 6
    PACKER_OWNED = 7


class Basis(IntEnum):
    ALL = 0
    CARCASS = 1
    LIVE = 2
