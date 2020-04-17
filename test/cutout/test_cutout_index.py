import json
from datetime import date
from itertools import starmap

from numpy import allclose
from numpy import isclose
from numpy import sum
from pandas import DataFrame
from pandas import concat
from pandas import pivot_table

from mpr.cutout.model import parse_record
from mpr.cutout.model import to_array

with open('test/resources/cutout.json') as resource:
    reports = json.load(resource)
    records = to_array(list(starmap(parse_record, zip(*reports))))


def test_daily_prices():
    record = records[records.date == date(2019, 2, 27)][0]
    assert isclose(record.carcass_price, 59.57)
    assert isclose(record.loin_price, 57.98)
    assert isclose(record.butt_price, 66.48)
    assert isclose(record.picnic_price, 34.76)
    assert isclose(record.rib_price, 110.69)
    assert isclose(record.ham_price, 45.24)
    assert isclose(record.belly_price, 97.67)


def test_cutout_index():
    loads = records.primal_loads + records.trimming_loads
    values = loads * records.carcass_price
    index = sum(values[-5:]) / sum(loads[-5:])
    assert isclose(index.round(decimals=2), 60.34)


def test_cutout_index_series():
    cutout = DataFrame(records, columns=['date', 'primal_loads', 'trimming_loads', 'carcass_price'])
    cutout = cutout.set_index('date').sort_values(by='date')

    loads = cutout.primal_loads + cutout.trimming_loads
    values = loads * cutout.carcass_price

    totals = pivot_table(concat([loads.rename('loads'), values.rename('value')], axis=1), index='date')
    rolling_totals = totals.rolling(5).sum().dropna()
    index = rolling_totals.value / rolling_totals.loads

    assert allclose(index.tail(10).round(decimals=2),
        (64.41, 64.09, 63.39, 62.04, 61.29, 61.02, 60.32, 60.19, 60.46, 60.34))
