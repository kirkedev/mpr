import json

from numpy import allclose

from mpr.slaughter.cash_index import cash_index_report
from mpr.slaughter.model import parse_record

with open('test/resources/cash_prices.json') as resource:
    records = map(parse_record, json.load(resource))
    barrows_gilts = cash_index_report(records).tail(10)


def test_daily_avg():
    daily_avg = barrows_gilts['Daily Avg Price']
    assert allclose(daily_avg, (56.40, 55.98, 55.78, 55.32, 55.16, 54.89, 54.64, 54.08, 54.19, 53.93))


def test_price_change():
    index_change = barrows_gilts['Price Change']
    assert allclose(index_change, (-0.25, -0.42, -0.20, -0.46, -0.16, -0.27, -0.25, -0.56, 0.11, -0.26))


def test_cme_index():
    cme_index = barrows_gilts['CME Index']
    assert allclose(cme_index, (56.53, 56.14, 55.91, 55.55, 55.24, 55.02, 54.74, 54.43, 54.13, 54.06))


def test_cme_change():
    index_change = barrows_gilts['Index Change']
    assert allclose(index_change, (-0.36, -0.39, -0.23, -0.36, -0.31, -0.22, -0.28, -0.31, -0.30, -0.07))
