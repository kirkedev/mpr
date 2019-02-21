from mpr.data.model.purchase_type import Seller
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.purchase_type import Basis


purchase_types = {
    'Negotiated (carcass basis)':
        (Seller.ALL.value, Arrangement.NEGOTIATED.value, Basis.CARCASS.value),

    'Negotiated Formula (carcass basis)':
        (Seller.ALL.value, Arrangement.NEGOTIATED_FORMULA.value, Basis.CARCASS.value),

    'Combined Negotiated/Negotiated Formula (carcass basis)':
        (Seller.ALL.value, Arrangement.ALL_NEGOTIATED.value, Basis.CARCASS.value),

    'Swine/Pork Market Formula (carcass basis)':
        (Seller.ALL.value, Arrangement.MARKET_FORMULA.value, Basis.CARCASS.value),

    'Negotiated (live basis)':
        (Seller.ALL.value, Arrangement.NEGOTIATED.value, Basis.LIVE.value),

    'Negotiated Formula (live basis)':
        (Seller.ALL.value, Arrangement.NEGOTIATED_FORMULA.value, Basis.LIVE.value),

    'Combined Negotiated/Negotiated Formula (live basis)':
        (Seller.ALL.value, Arrangement.ALL_NEGOTIATED.value, Basis.LIVE.value),

    'Prod. Sold Negotiated':
        (Seller.PRODUCER.value, Arrangement.NEGOTIATED.value, Basis.ALL.value),

    'Prod. Sold Other Market Formula':
        (Seller.PRODUCER.value, Arrangement.OTHER_MARKET_FORMULA.value, Basis.ALL.value),

    'Prod. Sold Swine/Pork Market Formula':
        (Seller.PRODUCER.value, Arrangement.MARKET_FORMULA.value, Basis.ALL.value),

    'Prod. Sold Other Purchase Arrangement':
        (Seller.PRODUCER.value, Arrangement.OTHER_PURCHASE.value, Basis.ALL.value),

    'Prod. Sold Negotiated Formula':
        (Seller.PRODUCER.value, Arrangement.NEGOTIATED_FORMULA.value, Basis.ALL.value),

    'Pack. Sold (all purchase types)':
        (Seller.PACKER.value, Arrangement.ALL.value, Basis.ALL.value)
}
