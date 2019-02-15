from typing import NamedTuple

from tables import IsDescription
from tables import EnumCol

from .enum_field import EnumField


class Seller(EnumField):
    PRODUCER = 'producer'
    PACKER = 'packer'
    ALL = 'all'


class Arrangement(EnumField):
    NEGOTIATED = 'negotiated'
    MARKET_FORMULA = 'market formula'
    NEGOTIATED_FORMULA = 'negotiated formula'
    OTHER_MARKET_FORMULA = 'other market formula'
    OTHER_PURCHASE = 'other'
    ALL = 'all'
    ALL_NEGOTIATED = 'all negotiated'

    PACKER_OWNED = 'packer owned'
    PACKER_SOLD = 'packer sold'


class Basis(EnumField):
    CARCASS = 'carcass'
    LIVE = 'live'


class PurchaseType(NamedTuple):
    seller: Seller
    arrangements: Arrangement
    basis: Basis


class PurchaseTypeCol(IsDescription):
    seller = EnumCol(Seller.values(), 'all', base='uint8')
    arrangement = EnumCol(Arrangement.values(), 'all', base='uint8')
    basis = EnumCol(Basis.values(), 'carcass', base='uint8')


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
