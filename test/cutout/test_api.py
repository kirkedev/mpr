from datetime import date
from numpy import isclose

from mpr.cutout.api import parse_attributes
from mpr.cutout.model import to_array

from test import load_resource

attributes = load_resource('api/cutout.xml')
cutout = parse_attributes(next(attributes), next(attributes))


def test_parse_report():
    assert cutout.date == date(2018, 8, 20)
    assert cutout.report_date == date(2018, 8, 20)
    assert isclose(cutout.primal_loads, 334.74)
    assert isclose(cutout.trimming_loads, 39.61)
    assert isclose(cutout.carcass_price, 67.18)
    assert isclose(cutout.loin_price, 75.51)
    assert isclose(cutout.butt_price, 89.55)
    assert isclose(cutout.picnic_price, 41.82)
    assert isclose(cutout.rib_price, 113.95)
    assert isclose(cutout.ham_price, 57.52)
    assert isclose(cutout.belly_price, 77.77)
    assert isclose(cutout.loads, 374.35)
    assert isclose(cutout.value, 25148.83)


def test_record_array():
    records = to_array([cutout])
    assert len(records) == 1
    assert all(records.date == date(2018, 8, 20))
