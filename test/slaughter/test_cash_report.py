from numpy import allclose

from mpr.slaughter.api import filter_section
from mpr.slaughter.api import parse_attributes
from mpr.cash_index.report import cash_index_report
from mpr.reports import SlaughterReport

from test import load_resource

report = filter_section(load_resource('reports/cash_prices.xml'), SlaughterReport.Section.BARROWS_AND_GILTS)
records = map(parse_attributes, report)
report = cash_index_report(records).tail(10)


def test_daily_avg():
    daily_avg = report['Daily Avg Price']
    assert allclose(daily_avg, (56.40, 55.98, 55.78, 55.32, 55.16, 54.89, 54.64, 54.08, 54.19, 53.93))


def test_price_change():
    index_change = report['Price Change']
    assert allclose(index_change, (-0.25, -0.42, -0.20, -0.46, -0.16, -0.27, -0.25, -0.56, 0.11, -0.26))


def test_cme_index():
    cme_index = report['CME Index']
    assert allclose(cme_index, (56.53, 56.14, 55.91, 55.55, 55.24, 55.02, 54.74, 54.43, 54.13, 54.06))


def test_cme_change():
    index_change = report['Index Change']
    assert allclose(index_change, (-0.36, -0.39, -0.23, -0.36, -0.31, -0.22, -0.28, -0.31, -0.30, -0.07))
