import json
from itertools import chain

from numpy import isclose
from numpy import nansum

from mpr.sales.model import parse_record
from mpr.sales.bacon_index import fresh_bacon
from mpr.sales.model import to_array

# https://www.cmegroup.com/trading/agricultural/livestock/cme-fresh-bacon-index.html

with open('test/resources/bellies_negotiated.json') as resource:
    negotiated = map(parse_record, json.load(resource))


with open('test/resources/bellies_formula.json') as resource:
    formula = map(parse_record, json.load(resource))

records = to_array(chain(filter(fresh_bacon, negotiated), filter(fresh_bacon, formula)))


def test_9_pound_bacon():
    cut = records.description == 'Derind Belly 7-9#'
    weight = records[cut].weight
    value = weight * records[cut].avg_price

    assert weight.sum() == 3_614 + 240_542
    assert isclose(value.sum(), 37_555_655.82)


def test_13_pound_bacon():
    cut = records.description == 'Derind Belly 9-13#'
    weight = records[cut].weight
    value = weight * records[cut].avg_price

    assert weight.sum() == 957_318 + 6_071_771
    assert isclose(value.sum(), 1_095_896_617.54)


def test_17_pound_bacon():
    cut = records.description == 'Derind Belly 13-17#'
    weight = records[cut].weight
    value = weight * records[cut].avg_price

    assert weight.sum() == 1_048_913 + 7_979_498
    assert isclose(value.sum(), 1_393_176_115.96)


def test_19_pound_bacon():
    cut = records.description == 'Derind Belly 17-19#'
    weight = records[cut].weight
    value = weight * records[cut].avg_price

    assert weight.sum() == 139_850 + 540_206
    assert isclose(value.sum(), 98_157_994.94)


def test_bacon_index():
    weight = nansum(records.weight)
    values = (records.weight * records.avg_price).round(decimals=2)
    total_value = nansum(values)
    index = total_value / weight

    assert weight == 16_981_712
    assert isclose(total_value.round(), 2_624_786_384)
    assert isclose(index.round(decimals=2), 154.57)
