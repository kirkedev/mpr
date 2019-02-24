from unittest import TestCase
from numpy import allclose
from numpy import round

from mpr.data.api.slaughter import parse_attributes
from mpr.cash_prices import cash_index
from mpr.cash_prices import filter_types
from . import load_resource

records = filter_types(map(parse_attributes, load_resource('cash_prices.xml')))
report = cash_index(records).tail(10)


class TestCashPrices(TestCase):
    # Values collected from daily CME Lean Hog Index Reports:
    # ftp://ftp.cmegroup.com/cash_settled_commodity_index_prices/daily_data/lean_hogs/
    def test_daily_avg(self):
        daily_avg = report['Daily Avg Price']
        self.assertTrue(allclose(round(daily_avg, decimals=2),
            (56.40, 55.98, 55.78, 55.32, 55.16, 54.89, 54.64, 54.08, 54.19, 53.93)))

    def test_price_change(self):
        index_change = report['Price Change']
        self.assertTrue(allclose(round(index_change, decimals=2),
             (-0.25, -0.42, -0.20, -0.46, -0.16, -0.27, -0.25, -0.56, 0.11, -0.26)))

    def test_cme_index(self):
        cme_index = report['CME Index']
        self.assertTrue(allclose(round(cme_index, decimals=2),
            (56.53, 56.14, 55.91, 55.55, 55.24, 55.02, 54.74, 54.43, 54.13, 54.06)))

    def test_cme_change(self):
        index_change = report['Index Change']
        self.assertTrue(allclose(round(index_change, decimals=2),
            (-0.36, -0.39, -0.23, -0.36, -0.31, -0.22, -0.28, -0.31, -0.30, -0.07)))
