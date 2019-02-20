from typing import NamedTuple

import numpy as np
from numpy import uint8


from . import EnumField


class Seller(EnumField):
    ALL = 'all'
    PRODUCER = 'producer'
    PACKER = 'packer'


class Arrangement(EnumField):
    ALL = 'all'
    NEGOTIATED = 'negotiated'
    MARKET_FORMULA = 'market formula'
    NEGOTIATED_FORMULA = 'negotiated formula'
    OTHER_MARKET_FORMULA = 'other market formula'
    OTHER_PURCHASE = 'other'
    ALL_NEGOTIATED = 'all negotiated'
    PACKER_OWNED = 'packer owned'


class Basis(EnumField):
    ALL = 'all'
    CARCASS = 'carcass'
    LIVE = 'live'


dtype = np.dtype([
    ('seller', uint8),
    ('arrangement', uint8),
    ('basis', uint8)
])

PurchaseType = type(dtype)
