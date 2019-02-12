from enum import Enum
from enum import unique
from typing import NamedTuple
from tables import IsDescription
from tables import EnumCol


@unique
class Seller(Enum):
    PRODUCER = 'producer'
    PACKER = 'packer'
    ALL = 'all'

    @staticmethod
    def from_ordinal(ordinal: int) -> 'Seller':
        return sellers[ordinal]

    def to_ordinal(self):
        return sellers.index(self)


@unique
class Arrangement(Enum):
    NEGOTIATED = 'negotiated'
    MARKET_FORMULA = 'market formula'
    NEGOTIATED_FORMULA = 'negotiated formula'
    OTHER_MARKET_FORMULA = 'other market formula'
    OTHER_PURCHASE = 'other'
    ALL = 'all'
    ALL_NEGOTIATED = 'all negotiated'

    PACKER_OWNED = 'packer owned'
    PACKER_SOLD = 'packer sold'

    @staticmethod
    def from_ordinal(ordinal: int) -> 'Arrangement':
        return arrangements[ordinal]

    def to_ordinal(self):
        return arrangements.index(self)


@unique
class Basis(Enum):
    CARCASS = 'carcass'
    LIVE = 'live'

    @staticmethod
    def from_ordinal(ordinal: int) -> 'Basis':
        return bases[ordinal]

    def to_ordinal(self):
        return bases.index(self)


class PurchaseType(NamedTuple):
    seller: Seller
    arrangements: Arrangement
    basis: Basis


class PurchaseTypeCol(IsDescription):
    seller = EnumCol([entry.value for entry in sellers], 'producer', base='uint8')
    arrangement = EnumCol([entry.value for entry in arrangements], 'negotiated', base='uint8')
    basis = EnumCol([entry.value for entry in bases], 'carcass', base='uint8')


sellers = list(Seller)
arrangements = list(Arrangement)
bases = list(Basis)

purchase_types = {
    'Negotiated (carcass basis)':
        PurchaseType(Seller.ALL, Arrangement.NEGOTIATED, Basis.CARCASS),

    'Negotiated Formula (carcass basis)':
        PurchaseType(Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),

    'Combined Negotiated/Negotiated Formula (carcass basis)':
        PurchaseType(Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.CARCASS),

    'Swine/Pork Market Formula (carcass basis)':
        PurchaseType(Seller.ALL, Arrangement.MARKET_FORMULA, Basis.CARCASS),

    'Negotiated (live basis)':
        PurchaseType(Seller.ALL, Arrangement.NEGOTIATED, Basis.LIVE),

    'Negotiated Formula (live basis)':
        PurchaseType(Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.LIVE),

    'Combined Negotiated/Negotiated Formula (live basis)':
        PurchaseType(Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.LIVE)

    # 'Prod. Sold Negotiated':

    # 'Prod. Sold Other Market Formula':

    # 'Prod. Sold Swine/Pork Market Formula':

    # 'Prod. Sold Other Purchase Arrangement':

    # 'Prod. Sold Negotiated Formula':

    # 'Pack. Sold (all purchase types)':
}
