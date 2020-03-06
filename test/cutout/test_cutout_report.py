import json
from itertools import starmap

from numpy import allclose

from mpr.cutout.api import parse_record
from mpr.cutout.cutout_index import cutout_report

with open('test/resources/cutout.json') as resource:
    reports = json.load(resource)
    report = cutout_report(starmap(parse_record, zip(*reports))).tail(10)


def test_carcass_price():
    carcass_price = report['Carcass Price']
    assert allclose(carcass_price,
         (62.76, 63.03, 61.58, 59.91, 60.17, 61.23, 59.01, 60.92, 60.96, 59.57))


def test_cutout_index():
    cutout_index = report['Cutout Index']
    assert allclose(cutout_index,
         (64.41, 64.09, 63.39, 62.04, 61.29, 61.02, 60.32, 60.19, 60.46, 60.34))
