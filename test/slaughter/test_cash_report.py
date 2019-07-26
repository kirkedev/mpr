from unittest import TestCase
from numpy import allclose

from mpr.slaughter.api import filter_section
from mpr.slaughter.api import parse_attributes
from mpr.cash_index.report import cash_index_report
from mpr.reports import SlaughterSection

from test import load_resource

report = filter_section(load_resource('reports/cash_prices.xml'), SlaughterSection.BARROWS_AND_GILTS)
records = map(parse_attributes, report)
report = cash_index_report(records).tail(10)


class TestCashPrices(TestCase):
    # Values collected from daily CME Lean Hog Index Reports:
    # ftp://ftp.cmegroup.com/cash_settled_commodity_index_prices/daily_data/lean_hogs/

    def test_daily_avg(self):
        daily_avg = report['Daily Avg Price']
        self.assertTrue(allclose(daily_avg, (56.40, 55.98, 55.78, 55.32, 55.16, 54.89, 54.64, 54.08, 54.19, 53.93)))

    def test_price_change(self):
        index_change = report['Price Change']
        self.assertTrue(allclose(index_change, (-0.25, -0.42, -0.20, -0.46, -0.16, -0.27, -0.25, -0.56, 0.11, -0.26)))

    def test_cme_index(self):
        cme_index = report['CME Index']
        self.assertTrue(allclose(cme_index, (56.53, 56.14, 55.91, 55.55, 55.24, 55.02, 54.74, 54.43, 54.13, 54.06)))

    def test_cme_change(self):
        index_change = report['Index Change']
        self.assertTrue(allclose(index_change, (-0.36, -0.39, -0.23, -0.36, -0.31, -0.22, -0.28, -0.31, -0.30, -0.07)))
