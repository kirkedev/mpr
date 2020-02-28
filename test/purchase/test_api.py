from datetime import date
from numpy import isnan
from numpy import isclose

from mpr.purchase.api import parse_attributes
from mpr.purchase.model import to_array
from mpr.purchase_type import Seller, Arrangement, Basis

from test import load_resource

negotiated, negotiated_formula, *_ = map(parse_attributes, load_resource('api/purchase.xml'))


def test_negotiated_purchase():
    assert negotiated.date == date(2019, 1, 31)
    assert negotiated.report_date == date(2019, 2, 1)
    assert negotiated.seller == Seller.ALL
    assert negotiated.arrangement == Arrangement.NEGOTIATED
    assert negotiated.basis == Basis.CARCASS
    assert negotiated.head_count == 11325
    assert isclose(negotiated.avg_price, 50.7)
    assert isclose(negotiated.low_price, 48.0)
    assert isclose(negotiated.high_price, 51.75)


def test_negotiated_formula():
    assert negotiated_formula.date, date(2019, 1, 31)
    assert negotiated_formula.arrangement, Arrangement.NEGOTIATED_FORMULA
    assert negotiated_formula.head_count, 165
    assert isnan(negotiated_formula.avg_price)
    assert isnan(negotiated_formula.low_price)
    assert isnan(negotiated_formula.high_price)


def test_record_array():
    records = to_array([negotiated, negotiated_formula])
    assert len(records) == 2
    assert all(records.date == date(2019, 1, 31))
