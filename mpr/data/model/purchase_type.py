from typing import NamedTuple
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
    PACKER_SOLD = 'packer sold'


class Basis(EnumField):
    ALL = 'all'
    CARCASS = 'carcass'
    LIVE = 'live'


class PurchaseType(NamedTuple):
    seller: Seller
    arrangements: Arrangement
    basis: Basis


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
        PurchaseType(Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.LIVE),

    'Prod. Sold Negotiated':
        PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.ALL),

    'Prod. Sold Other Market Formula':
        PurchaseType(Seller.PRODUCER, Arrangement.OTHER_MARKET_FORMULA, Basis.ALL),

    'Prod. Sold Swine/Pork Market Formula':
        PurchaseType(Seller.PRODUCER, Arrangement.MARKET_FORMULA, Basis.ALL),

    'Prod. Sold Other Purchase Arrangement':
        PurchaseType(Seller.PRODUCER, Arrangement.OTHER_PURCHASE, Basis.ALL),

    'Prod. Sold Negotiated Formula':
        PurchaseType(Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.ALL),

    'Pack. Sold (all purchase types)':
        PurchaseType(Seller.PACKER, Arrangement.ALL, Basis.ALL)
}
