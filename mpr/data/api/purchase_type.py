from mpr.data.model.purchase_type import Seller
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.purchase_type import Basis


purchase_types = {
    'Negotiated (carcass basis)':
        (Seller.ALL.to_ordinal(), Arrangement.NEGOTIATED.to_ordinal(), Basis.CARCASS.to_ordinal()),

    'Negotiated Formula (carcass basis)':
        (Seller.ALL.to_ordinal(), Arrangement.NEGOTIATED_FORMULA.to_ordinal(), Basis.CARCASS.to_ordinal()),

    'Combined Negotiated/Negotiated Formula (carcass basis)':
        (Seller.ALL.to_ordinal(), Arrangement.ALL_NEGOTIATED.to_ordinal(), Basis.CARCASS.to_ordinal()),

    'Swine/Pork Market Formula (carcass basis)':
        (Seller.ALL.to_ordinal(), Arrangement.MARKET_FORMULA.to_ordinal(), Basis.CARCASS.to_ordinal()),

    'Negotiated (live basis)':
        (Seller.ALL.to_ordinal(), Arrangement.NEGOTIATED.to_ordinal(), Basis.LIVE.to_ordinal()),

    'Negotiated Formula (live basis)':
        (Seller.ALL.to_ordinal(), Arrangement.NEGOTIATED_FORMULA.to_ordinal(), Basis.LIVE.to_ordinal()),

    'Combined Negotiated/Negotiated Formula (live basis)':
        (Seller.ALL.to_ordinal(), Arrangement.ALL_NEGOTIATED.to_ordinal(), Basis.LIVE.to_ordinal()),

    'Prod. Sold Negotiated':
        (Seller.PRODUCER.to_ordinal(), Arrangement.NEGOTIATED.to_ordinal(), Basis.ALL.to_ordinal()),

    'Prod. Sold Other Market Formula':
        (Seller.PRODUCER.to_ordinal(), Arrangement.OTHER_MARKET_FORMULA.to_ordinal(), Basis.ALL.to_ordinal()),

    'Prod. Sold Swine/Pork Market Formula':
        (Seller.PRODUCER.to_ordinal(), Arrangement.MARKET_FORMULA.to_ordinal(), Basis.ALL.to_ordinal()),

    'Prod. Sold Other Purchase Arrangement':
        (Seller.PRODUCER.to_ordinal(), Arrangement.OTHER_PURCHASE.to_ordinal(), Basis.ALL.to_ordinal()),

    'Prod. Sold Negotiated Formula':
        (Seller.PRODUCER.to_ordinal(), Arrangement.NEGOTIATED_FORMULA.to_ordinal(), Basis.ALL.to_ordinal()),

    'Pack. Sold (all purchase types)':
        (Seller.PACKER.to_ordinal(), Arrangement.ALL.to_ordinal(), Basis.ALL.to_ordinal())
}
