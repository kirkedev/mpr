from abc import ABC
from datetime import date

from numpy import datetime64
from tables import Time32Col
from tables import Float32Col
from tables.tableextension import Row

from mpr.data.model.cutout import Cutout
from .observation import Observation


class CutoutEntity(Observation[Cutout], ABC):
    schema = {
        'date': Time32Col(),
        'primal_loads': Float32Col(),
        'trimming_loads': Float32Col(),
        'carcass_price': Float32Col(),
        'loin_price': Float32Col(),
        'butt_price': Float32Col(),
        'picnic_price': Float32Col(),
        'rib_price': Float32Col(),
        'ham_price': Float32Col(),
        'belly_price': Float32Col()
    }

    @classmethod
    def from_row(cls, row: Row) -> Cutout:
        return Cutout(
            date=datetime64(date.fromordinal(row['date']), 'D'),
            primal_loads=row['primal_loads'],
            trimming_loads=row['trimming_loads'],
            carcass_price=row['carcass_price'],
            loin_price=row['loin_price'],
            butt_price=row['butt_price'],
            picnic_price=row['picnic_price'],
            rib_price=row['rib_price'],
            ham_price=row['ham_price'],
            belly_price=row['belly_price'])

    @classmethod
    def append(cls, record: Cutout):
        row = cls.table.row

        row['date'] = record.date.astype(date).to_ordinal()
        row['primal_loads'] = record.primal_loads
        row['trimming_loads'] = record.trimming_loads
        row['carcass_price'] = record.carcass_price
        row['loin_price'] = record.loin_price
        row['butt_price'] = record.butt_price
        row['picnic_price'] = record.picnic_price
        row['rib_price'] = record.rib_price
        row['ham_price'] = record.ham_price
        row['belly_price'] = record.belly_price

        row.append()
