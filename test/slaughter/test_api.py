from datetime import date
from numpy import isnan
from numpy import isclose

from mpr.slaughter.api import parse_attributes
from mpr.slaughter.model import to_array
from mpr.purchase_type import Seller, Arrangement, Basis

from test import load_resource

attributes = list(load_resource('api/slaughter.xml'))
assert len(attributes) == 8

negotiated = parse_attributes(attributes[0])
negotiated_formula = parse_attributes(attributes[4])


def test_negotiated():
    assert negotiated.date == date(2019, 2, 1)
    assert negotiated.report_date == date(2019, 2, 4)
    assert negotiated.seller == Seller.PRODUCER
    assert negotiated.arrangement == Arrangement.NEGOTIATED
    assert negotiated.basis == Basis.ALL
    assert isclose(negotiated.head_count, 12771)
    assert isclose(negotiated.base_price, 51.8)
    assert isclose(negotiated.net_price, 53.26)
    assert isclose(negotiated.low_price, 43.57)
    assert isclose(negotiated.high_price, 57.85)
    assert isclose(negotiated.live_weight, 273.54)
    assert isclose(negotiated.carcass_weight, 205.41)
    assert isclose(negotiated.sort_loss, -2.16)
    assert isclose(negotiated.backfat, 0.61)
    assert isclose(negotiated.loin_depth, 2.61)
    assert isclose(negotiated.loineye_area, 7.83)
    assert isclose(negotiated.lean_percent, 55.6)
    assert isclose(negotiated.total_weight, 2623291.16)
    assert isclose(negotiated.total_value, 139716484.52)
    assert isclose(negotiated.avg_price, 53.26)


def test_negotiated_formula():
    assert negotiated_formula.date == date(2019, 2, 1)
    assert negotiated_formula.arrangement == Arrangement.NEGOTIATED_FORMULA
    assert negotiated_formula.head_count == 683
    assert isnan(negotiated_formula.base_price)
    assert isnan(negotiated_formula.net_price)
    assert isnan(negotiated_formula.low_price)
    assert isnan(negotiated_formula.high_price)
    assert isnan(negotiated_formula.live_weight)
    assert isnan(negotiated_formula.carcass_weight)
    assert isnan(negotiated_formula.sort_loss)
    assert isnan(negotiated_formula.backfat)
    assert isnan(negotiated_formula.loin_depth)
    assert isnan(negotiated_formula.loineye_area)
    assert isnan(negotiated_formula.lean_percent)
    assert isnan(negotiated_formula.total_weight)
    assert isnan(negotiated_formula.total_value)
    assert isnan(negotiated_formula.avg_price)


def test_record_array():
    records = to_array([negotiated, negotiated_formula])
    assert len(records) == 2
    assert all(records.date == date(2019, 2, 1))
