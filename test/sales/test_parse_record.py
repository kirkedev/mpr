import json
from datetime import date

from numpy import isclose
from numpy import isnan

from mpr.sales.cut import Cut
from mpr.sales.model import parse_record

with open('test/resources/sales.json') as resource:
    bacon = map(parse_record, json.load(resource))


def test_first():
    record = next(bacon)
    assert record.report == 'lm_pk602'
    assert record.type == Cut.BELLY
    assert record.date == date(2019, 2, 1)
    assert record.description == 'Derind Belly 13-17#'
    assert record.weight == 151_772
    assert isclose(record.avg_price, 137.74)
    assert isclose(record.low_price, 136.76)
    assert isclose(record.high_price, 140.50)


def test_second():
    record = next(bacon)
    assert record.report == 'lm_pk602'
    assert record.type == Cut.BELLY
    assert record.date == date(2019, 2, 1)
    assert record.description == 'Derind Belly 17-19#'
    assert record.weight == 0
    assert isnan(record.avg_price)
    assert isnan(record.low_price)
    assert isnan(record.high_price)


def test_third():
    record = next(bacon)
    assert record.report == 'lm_pk602'
    assert record.type == Cut.BELLY
    assert record.date == date(2019, 2, 1)
    assert record.description == 'Derind Belly 7-9#'
    assert record.weight == 0
    assert isnan(record.avg_price)
    assert isnan(record.low_price)
    assert isnan(record.high_price)


def test_fourth():
    record = next(bacon)
    assert record.report == 'lm_pk602'
    assert record.type == Cut.BELLY
    assert record.date == date(2019, 2, 1)
    assert record.description == 'Derind Belly 9-13#'
    assert record.weight == 35_620
    assert isclose(record.avg_price, 142.71)
    assert isclose(record.low_price, 140.50)
    assert isclose(record.high_price, 152.00)
