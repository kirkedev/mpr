from unittest import TestCase
from numpy import allclose

from mpr.cutout.api import filter_sections
from mpr.cutout.api import parse_attributes
from mpr.cutout_index.report import cutout_report
from mpr.reports import CutoutSection

from test import load_resource

report = filter_sections(load_resource('reports/cutout.xml'), CutoutSection.CUTOUT, CutoutSection.VOLUME)
records = map(lambda it: parse_attributes(*it), report)
report = cutout_report(records).tail(10)


class TestCutoutReport(TestCase):
    def test_carcass_price(self):
        carcass_price = report['Carcass Price']
        self.assertTrue(allclose(carcass_price,
             (62.76, 63.03, 61.58, 59.91, 60.17, 61.23, 59.01, 60.92, 60.96, 59.57)))

    def test_cutout_index(self):
        cutout_index = report['Cutout Index']
        self.assertTrue(allclose(cutout_index,
             (64.41, 64.09, 63.39, 62.04, 61.29, 61.02, 60.32, 60.19, 60.46, 60.34)))
