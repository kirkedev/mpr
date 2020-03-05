from typing import Iterator

import pandas as pd
from pandas import Series
from pandas import DataFrame

from ..report import create_table
from ..report import with_change
from ..cutout.model import Cutout
from ..cutout.model import to_array


def cutout_index(loads: Series, carcass_price: Series) -> Series:
    values = loads * carcass_price
    pivot_table = pd.pivot_table(create_table(loads.rename('loads'), values.rename('value')), index='date')
    rolling_totals = pivot_table.rolling(5).sum().dropna()

    return rolling_totals.value / rolling_totals.loads


def cutout_report(records: Iterator[Cutout]) -> DataFrame:
    data = DataFrame(to_array(records)).set_index('date').sort_values(by='date')

    loads = data.primal_loads + data.trimming_loads
    carcass_price, price_change = with_change(data.carcass_price)
    index, index_change = with_change(cutout_index(loads, carcass_price))

    return create_table(
        index.rename('Cutout Index'),
        index_change.rename('Index Change'),
        carcass_price.rename('Carcass Price'),
        price_change.rename('Price Change'),
        loads.rename('Total Loads'),
        data.loin_price.rename('Loin Price'),
        data.belly_price.rename('Belly Price'),
        data.butt_price.rename('Butt Price'),
        data.ham_price.rename('Ham Price'),
        data.rib_price.rename('Rib Price'),
        data.picnic_price.rename('Picnic Price'))
