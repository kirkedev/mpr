from typing import Dict

from ..purchase_type import Arrangement
from ..purchase_type import Basis
from ..purchase_type import PurchaseType
from ..purchase_type import Seller

purchase_types: Dict[str, PurchaseType] = {
    'Negotiated (carcass basis)':
        (Seller.ALL, Arrangement.NEGOTIATED, Basis.CARCASS),

    'Negotiated Formula (carcass basis)':
        (Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),

    'Swine/Pork Market Formula (carcass basis)':
        (Seller.ALL, Arrangement.MARKET_FORMULA, Basis.CARCASS),

    'Negotiated (live basis)':
        (Seller.ALL, Arrangement.NEGOTIATED, Basis.LIVE),

    'Negotiated Formula (live basis)':
        (Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.LIVE),

    'Combined Negotiated/Negotiated Formula (carcass basis)':
        (Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.CARCASS),

    'Combined Negotiated/Negotiated Formula (live basis)':
        (Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.LIVE)
}
