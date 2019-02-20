from unittest import TestCase
from datetime import date
from numpy import isclose

from test.api import load_resource
from mpr.data.model.cutout import Record
from mpr.data.model.cutout import to_array

attributes = load_resource('test/api/resources/cutout.xml')
cutout = Record.from_attributes(next(attributes), next(attributes))
records = to_array([cutout])


class CutoutTest(TestCase):
    def test_parse_date(self):
        self.assertEqual(cutout.date, date(2018, 8, 20))

    def test_primal_loads(self):
        self.assertTrue(isclose(cutout.primal_loads, 334.74))

    def test_trimming_loads(self):
        self.assertTrue(isclose(cutout.trimming_loads, 39.61))

    def test_parse_carcass_price(self):
        self.assertTrue(isclose(cutout.carcass_price, 67.18))

    def test_loin_price(self):
        self.assertTrue(isclose(cutout.loin_price, 75.51))

    def test_butt_price(self):
        self.assertTrue(isclose(cutout.butt_price, 89.55))

    def test_picnic_price(self):
        self.assertTrue(isclose(cutout.picnic_price, 41.82))

    def test_rib_price(self):
        self.assertTrue(isclose(cutout.rib_price, 113.95))

    def test_ham_price(self):
        self.assertTrue(isclose(cutout.ham_price, 57.52))

    def test_belly_price(self):
        self.assertTrue(isclose(cutout.belly_price, 77.77))


class TestRecordArray(TestCase):
    def test_length(self):
        self.assertEqual(len(records), 1)

    def test_index(self):
        self.assertTrue(all(records.date == date(2018, 8, 20)))
