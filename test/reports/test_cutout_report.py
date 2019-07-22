from unittest import TestCase
from numpy import allclose

from mpr.cutout.api import filter_sections
from mpr.cutout.api import parse_attributes
from mpr.cutout_index.report import cutout_report
from mpr.reports  import CutoutSection

from . import load_resource

# Given an Afternoon Cutout Report from Feb 27, 2019
report = filter_sections(load_resource('cutout.xml'), CutoutSection.CUTOUT, CutoutSection.VOLUME)
records = map(lambda it: parse_attributes(*it), report)

# When I run a cutout index report for the last 10 days
report = cutout_report(records).tail(10)


class TestCutoutReport(TestCase):
    # Then I should see the Daily Carcass Price
    def test_carcass_price(self):
        carcass_price = report['Carcass Price']
        self.assertTrue(allclose(carcass_price,
             (62.76, 63.03, 61.58, 59.91, 60.17, 61.23, 59.01, 60.92, 60.96, 59.57)))

    # And I should see the Cutout Index
    def test_cutout_index(self):
        cutout_index = report['Cutout Index']
        self.assertTrue(allclose(cutout_index,
             (64.41, 64.09, 63.39, 62.04, 61.29, 61.02, 60.32, 60.19, 60.46, 60.34)))

    # And I should see the change from the previous day
    def skip_test_price_change(self):
        index_change = report['Index Change']
        self.assertTrue(allclose(index_change, (-0.48, -0.35, -0.70, -1.34, -0.75, -0.27, -0.69, -0.13, 0.27, -0.12)))

    # And I should see the change from the previous day
    def skip_test_cme_change(self):
        index_change = report['Index Change']
        self.assertTrue(allclose(index_change, (-0.36, -0.39, -0.23, -0.36, -0.31, -0.22, -0.28, -0.31, -0.30, -0.07)))
