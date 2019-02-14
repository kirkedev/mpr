from abc import ABC
from dataclasses import dataclass
from typing import Optional
from typing import TypeVar
from datetime import date

from tables import UInt32Col
from tables import Float32Col
from tables.tableextension import Row

from .observation import Observation
from .purchase_type import Seller
from .purchase_type import Arrangement
from .purchase_type import Basis
from .purchase_type import PurchaseTypeCol

T = TypeVar('T', bound=Slaughter)


@dataclass
class Slaughter(ABC, Observation[T]):
    date: date
    seller: Seller
    arrangement: Arrangement
    basis: Basis
    head_count: int
    base_price: Optional[float]
    net_price: Optional[float]
    low_price: Optional[float]
    high_price: Optional[float]
    live_weight: Optional[float]
    carcass_weight: Optional[float]
    sort_loss: Optional[float]
    backfat: Optional[float]
    loin_depth: Optional[float]
    loineye_area: Optional[float]
    lean_percent: Optional[float]

    schema = {
        'date': UInt32Col(),
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

        row['date'] = self.date.toordinal()
        row['purchase_type/seller'] = self.seller.to_ordinal()
        row['purchase_type/arrangement'] = self.arrangement.to_ordinal()
        row['purchase_type/basis'] = self.basis.to_ordinal()
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
    def from_row(cls, row: Row) -> T:
        return cls(
            date=date.fromordinal(row['date']),
            seller=Seller.from_ordinal(row['purchase_type/seller']),
            arrangement=Arrangement.from_ordinal(row['purchase_type/arrangement']),
            basis=Basis.from_ordinal(row['purchase_type/basis']),
            head_count=row['head_count'],
            base_price=row['base_price'],
            net_price=row['net_price'],
            low_price=row['low_price'],
            high_price=row['high_price'],
            live_weight=row['live_weight'],
            carcass_weight=row['carcass_weight'],
            sort_loss=row['sort_loss'],
            backfat=row['backfat'],
            loin_depth=row['loin_depth'],
            loineye_area=row['loineye_area'],
            lean_percent=row['lean_percent'])
