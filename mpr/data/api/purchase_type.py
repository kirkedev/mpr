from mpr.data.model.purchase_type import Seller
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.purchase_type import Basis


purchase_types = {
    'Negotiated (carcass basis)':
        (Seller.ALL, Arrangement.NEGOTIATED, Basis.CARCASS),

    'Negotiated Formula (carcass basis)':
        (Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.CARCASS),

    'Combined Negotiated/Negotiated Formula (carcass basis)':
        (Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.CARCASS),

    'Swine/Pork Market Formula (carcass basis)':
        (Seller.ALL, Arrangement.MARKET_FORMULA, Basis.CARCASS),

    'Negotiated (live basis)':
        (Seller.ALL, Arrangement.NEGOTIATED, Basis.LIVE),

    'Negotiated Formula (live basis)':
        (Seller.ALL, Arrangement.NEGOTIATED_FORMULA, Basis.LIVE),

    'Combined Negotiated/Negotiated Formula (live basis)':
        (Seller.ALL, Arrangement.ALL_NEGOTIATED, Basis.LIVE),

    'Prod. Sold Negotiated':
        (Seller.PRODUCER, Arrangement.NEGOTIATED, Basis.ALL),

    'Prod. Sold Other Market Formula':
        (Seller.PRODUCER, Arrangement.OTHER_MARKET_FORMULA, Basis.ALL),

    'Prod. Sold Swine/Pork Market Formula':
        (Seller.PRODUCER, Arrangement.MARKET_FORMULA, Basis.ALL),

    'Prod. Sold Other Purchase Arrangement':
        (Seller.PRODUCER, Arrangement.OTHER_PURCHASE, Basis.ALL),

    'Prod. Sold Negotiated Formula':
        (Seller.PRODUCER, Arrangement.NEGOTIATED_FORMULA, Basis.ALL),

    'Pack. Sold (all purchase types)':
        (Seller.PACKER, Arrangement.ALL, Basis.ALL)
}
