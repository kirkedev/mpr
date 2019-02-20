from abc import ABC
from typing import NamedTuple
from typing import Iterator
from datetime import date
from datetime import datetime

import numpy as np
from numpy import datetime64
from numpy import float32
from numpy import recarray

from tables import Time32Col
from tables import Float32Col
from tables.tableextension import Row

from . import Attributes
from . import Date

from .observation import Observation

date_format = "%m/%d/%Y"


class Record(NamedTuple):
    date: Date
    primal_loads: float32
    trimming_loads: float32
    carcass_price: float32
    loin_price: float32
    butt_price: float32
    picnic_price: float32
    rib_price: float32
    ham_price: float32
    belly_price: float32

    @classmethod
    def from_attributes(cls, volume: Attributes, cutout: Attributes) -> 'Record':
        report_date = datetime.strptime(volume['report_date'], date_format).date()

        return cls(
            date=datetime64(report_date, 'D'),
            primal_loads=float32(volume['temp_cuts_total_load']),
            trimming_loads=float32(volume['temp_process_total_load']),
            carcass_price=float32(cutout['pork_carcass']),
            loin_price=float32(cutout['pork_loin']),
            butt_price=float32(cutout['pork_butt']),
            picnic_price=float32(cutout['pork_picnic']),
            rib_price=float32(cutout['pork_rib']),
            ham_price=float32(cutout['pork_ham']),
            belly_price=float32(cutout['pork_belly']))


dtype = np.dtype(list(Record._field_types.items()))


def to_array(records: Iterator[Record]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)


class Cutout(Record, Observation, ABC):
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
    def from_row(cls, row: Row) -> 'Cutout':
        return cls(
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

    def append(self):
        row = self.table.row

        row['date'] = self.date.astype(date).to_ordinal()
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
