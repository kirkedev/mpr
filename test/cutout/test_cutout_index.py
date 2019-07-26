from unittest import TestCase
from datetime import date
import numpy as np
import pandas as pd

from mpr.cutout.api import filter_sections
from mpr.cutout.api import parse_attributes
from mpr.cutout.model import to_array
from mpr.reports import CutoutSection

from test import load_resource

report = filter_sections(load_resource('reports/cutout.xml'), CutoutSection.VOLUME, CutoutSection.CUTOUT)
records = to_array(map(lambda it: parse_attributes(*it), report))


class TestCutoutIndex(TestCase):
    def test_daily_prices(self):
        last = records[records.date == date(2019, 2, 27)][0]
        self.assertTrue(np.isclose(last.carcass_price, 59.57))
        self.assertTrue(np.isclose(last.loin_price, 57.98))
        self.assertTrue(np.isclose(last.butt_price, 66.48))
        self.assertTrue(np.isclose(last.picnic_price, 34.76))
        self.assertTrue(np.isclose(last.rib_price, 110.69))
        self.assertTrue(np.isclose(last.ham_price, 45.24))
        self.assertTrue(np.isclose(last.belly_price, 97.67))

    def test_cutout_index(self):
        ascending = records[::-1]
        loads = ascending.primal_loads + ascending.trimming_loads
        values = loads * ascending.carcass_price
        index = np.sum(values[-5:]) / np.sum(loads[-5:])
        self.assertTrue(np.isclose(index.round(decimals=2), 60.34))

    def test_cutout_index_series(self):
        cutout = pd.DataFrame(records, columns=['date', 'primal_loads', 'trimming_loads', 'carcass_price'])
        cutout = cutout.set_index('date').sort_values(by='date')

        loads = cutout.primal_loads + cutout.trimming_loads
        values = loads * cutout.carcass_price

        totals = pd.pivot_table(pd.concat([loads.rename('loads'), values.rename('value')], axis=1), index='date')
        rolling_totals = totals.rolling(5).sum().dropna()
        index = rolling_totals.value / rolling_totals.loads

        self.assertTrue(np.allclose(index.tail(10).round(decimals=2),
            (64.41, 64.09, 63.39, 62.04, 61.29, 61.02, 60.32, 60.19, 60.46, 60.34)))
