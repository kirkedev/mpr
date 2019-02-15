from abc import ABC
from dataclasses import dataclass
from datetime import date

from tables import UInt32Col
from tables import Float32Col
from tables.tableextension import Row

from .observation import Observation


@dataclass
class Cutout(Observation, ABC):
    date: date
    primal_loads: float
    trimming_loads: float
    carcass_price: float
    loin_price: float
    butt_price: float
    picnic_price: float
    rib_price: float
    ham_price: float
    belly_price: float

    schema = {
        'date': UInt32Col(),
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
    def from_row(cls, row: Row) -> 'Cutout':
        return cls(
            date=date.fromordinal(row['date']),
            primal_loads=row['primal_loads'],
            trimming_loads=row['trimming_loads'],
            carcass_price=row['carcass_price'],
            loin_price=row['loin_price'],
            butt_price=row['butt_price'],
            picnic_price=row['picnic_price'],
            rib_price=row['rib_price'],
            ham_price=row['ham_price'],
            belly_price=row['belly_price'])

    def append(self):
        row = self.table.row

        row['date'] = self.date.toordinal()
        row['primal_loads'] = self.primal_loads
        row['trimming_loads'] = self.trimming_loads
        row['carcass_price'] = self.carcass_price
        row['loin_price'] = self.loin_price
        row['butt_price'] = self.butt_price
        row['picnic_price'] = self.picnic_price
        row['rib_price'] = self.rib_price
        row['ham_price'] = self.ham_price
        row['belly_price'] = self.belly_price

        row.append()
