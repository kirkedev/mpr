from abc import ABC
from dataclasses import dataclass
from datetime import date

from numpy import uint8
from numpy import uint32
from numpy import float32
from numpy import datetime64

from tables import UInt32Col
from tables import Float32Col
from tables import Time32Col
from tables.tableextension import Row

from .observation import Observation
from .purchase_type import PurchaseType
from .purchase_type import PurchaseTypeCol


@dataclass
class Slaughter(Observation, ABC):
    date: datetime64
    seller: uint8
    arrangement: uint8
    basis: uint8
    purchase_type: PurchaseType
    head_count: uint32
    base_price: float32
    net_price: float32
    low_price: float32
    high_price: float32
    live_weight: float32
    carcass_weight: float32
    sort_loss: float32
    backfat: float32
    loin_depth: float32
    loineye_area: float32
    lean_percent: float32

    schema = {
        'date': Time32Col(),
        'purchase_type': PurchaseTypeCol(),
        'head_count': UInt32Col(),
        'base_price': Float32Col(),
        'net_price': Float32Col(),
        'low_price': Float32Col(),
        'high_price': Float32Col(),
        'live_weight': Float32Col(),
        'carcass_weight': Float32Col(),
        'sort_loss': Float32Col(),
        'backfat': Float32Col(),
        'loin_depth': Float32Col(),
        'loineye_area': Float32Col(),
        'lean_percent': Float32Col()
    }

    @property
    def total_weight(self) -> float:
        return self.head_count * self.carcass_weight if self.carcass_weight else 0.0

    @property
    def total_value(self) -> float:
        return self.total_weight * self.net_price if self.net_price else 0.0

    def append(self):
        row = self.table.row

        row['date'] = self.date
        row['purchase_type/seller'] = self.seller
        row['purchase_type/arrangement'] = self.arrangement
        row['purchase_type/basis'] = self.basis
        row['head_count'] = self.head_count
        row['base_price'] = self.base_price
        row['net_price'] = self.net_price
        row['low_price'] = self.low_price
        row['high_price'] = self.high_price
        row['live_weight'] = self.live_weight
        row['carcass_weight'] = self.carcass_weight
        row['sort_loss'] = self.sort_loss
        row['backfat'] = self.backfat
        row['loin_depth'] = self.loin_depth
        row['loineye_area'] = self.loineye_area
        row['lean_percent'] = self.lean_percent

        row.append()

    @classmethod
    def from_row(cls, row: Row) -> 'Slaughter':
        return cls(row.fetch_all_fields())
