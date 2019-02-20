from typing import NamedTuple
from typing import Iterator
from datetime import datetime

import numpy as np
from numpy import datetime64
from numpy import float32
from numpy import recarray

from . import Attributes
from . import Date

date_format = "%m/%d/%Y"


class Cutout(NamedTuple):
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
    def from_attributes(cls, volume: Attributes, cutout: Attributes) -> 'Cutout':
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


dtype = np.dtype(list(Cutout._field_types.items()))


def to_array(records: Iterator[Cutout]) -> recarray:
    return np.rec.array(list(records), dtype=dtype)
