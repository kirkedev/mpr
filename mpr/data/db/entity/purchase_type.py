from tables import IsDescription
from tables import EnumCol

from mpr.data.model.purchase_type import Seller
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.purchase_type import Basis


class PurchaseTypeCol(IsDescription):
    seller = EnumCol(Seller.values(), 'all', base='uint8', pos=0)
    arrangement = EnumCol(Arrangement.values(), 'all', base='uint8', pos=1)
    basis = EnumCol(Basis.values(), 'all', base='uint8', pos=2)
