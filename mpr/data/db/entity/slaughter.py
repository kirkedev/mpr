from abc import ABC
from typing import Iterator
from datetime import date

from numpy import datetime64
from tables import UInt32Col
from tables import Float32Col
from tables.tableextension import Row

from mpr.data.model.slaughter import Slaughter
from mpr.data.model.slaughter import to_array

from .observation import Observation
from .purchase_type import PurchaseTypeCol


class SlaughterEntity(Observation[Slaughter], ABC):
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

    @classmethod
    def from_row(cls, row: Row) -> Slaughter:
        return Slaughter(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            purchase_type=row['purchase_type'],
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

    @classmethod
    def append(cls, record: Slaughter):
        row = cls.table.row

        row['date'] = record.date.astype(date).toordinal()
        row['purchase_type'] = record.purchase_type
        row['head_count'] = record.head_count
        row['base_price'] = record.base_price
        row['net_price'] = record.net_price
        row['low_price'] = record.low_price
        row['high_price'] = record.high_price
        row['live_weight'] = record.live_weight
        row['carcass_weight'] = record.carcass_weight
        row['sort_loss'] = record.sort_loss
        row['backfat'] = record.backfat
        row['loin_depth'] = record.loin_depth
        row['loineye_area'] = record.loineye_area
        row['lean_percent'] = record.lean_percent

        row.append()

    @classmethod
    def append_rows(cls, records: Iterator[Slaughter]):
        cls.table.append(to_array(records))
        cls.commit()
