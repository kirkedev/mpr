from enum import Enum, unique
from typing import NamedTuple

@unique
class Seller(Enum):
  PRODUCER = 'producer'
  PACKER = 'packer'

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

@unique
class Basis(Enum):
  CARCASS = 'carcass'
  LIVE = 'live'

class PurchaseType(NamedTuple):
  seller: Seller
  arrangement: Arrangement
  basis: Basis
