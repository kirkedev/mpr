from unittest import TestCase
from datetime import date
from numpy import isnan
from numpy import isclose

from mpr.data.api.slaughter import parse_attributes
from mpr.data.model.slaughter import to_array
from mpr.data.model.purchase_type import Seller
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.purchase_type import Basis

from test.api import load_resource

attributes = list(load_resource('test/resources/api/slaughter.xml'))
assert len(attributes) == 8

negotiated = parse_attributes(attributes[0])
negotiated_formula = parse_attributes(attributes[4])
records = to_array([negotiated, negotiated_formula])


class NegotiatedPurchaseTest(TestCase):
    def test_date(self):
        self.assertEqual(negotiated.date, date(2019, 2, 1))

    def test_seller(self):
        self.assertEqual(negotiated.seller, Seller.PRODUCER)

    def test_arrangement(self):
        self.assertEqual(negotiated.arrangement, Arrangement.NEGOTIATED)

    def test_basis(self):
        self.assertEqual(negotiated.basis, Basis.ALL)

    def test_head_count(self):
        self.assertTrue(isclose(negotiated.head_count, 12771))

    def test_base_price(self):
        self.assertTrue(isclose(negotiated.base_price, 51.8))

    def test_net_price(self):
        self.assertTrue(isclose(negotiated.net_price, 53.26))

    def test_low_price(self):
        self.assertTrue(isclose(negotiated.low_price, 43.57))

    def test_high_price(self):
        self.assertTrue(isclose(negotiated.high_price, 57.85))

    def test_live_weight(self):
        self.assertTrue(isclose(negotiated.live_weight, 273.54))

    def test_carcass_weight(self):
        self.assertTrue(isclose(negotiated.carcass_weight, 205.41))

    def test_sort_loss(self):
        self.assertTrue(isclose(negotiated.sort_loss, -2.16))

    def test_backfat(self):
        self.assertTrue(isclose(negotiated.backfat, 0.61))

    def test_loin_depth(self):
        self.assertTrue(isclose(negotiated.loin_depth, 2.61))

    def test_loineye_area(self):
        self.assertTrue(isclose(negotiated.loineye_area, 7.83))

    def test_lean_percent(self):
        self.assertTrue(isclose(negotiated.lean_percent, 55.6))


class NegotiatedFormulaTest(TestCase):
    def test_date(self):
        self.assertEqual(negotiated_formula.date, date(2019, 2, 1))

    def test_arrangement(self):
        self.assertEqual(negotiated_formula.arrangement, Arrangement.NEGOTIATED_FORMULA)

    def test_head_count(self):
        self.assertEqual(negotiated_formula.head_count, 683)

    def test_base_price(self):
        self.assertTrue(isnan(negotiated_formula.base_price))

    def test_net_price(self):
        self.assertTrue(isnan(negotiated_formula.net_price))

    def test_low_price(self):
        self.assertTrue(isnan(negotiated_formula.low_price))

    def test_high_price(self):
        self.assertTrue(isnan(negotiated_formula.high_price))

    def test_live_weight(self):
        self.assertTrue(isnan(negotiated_formula.live_weight))

    def test_carcass_weight(self):
        self.assertTrue(isnan(negotiated_formula.carcass_weight))

    def test_sort_loss(self):
        self.assertTrue(isnan(negotiated_formula.sort_loss))

    def test_backfat(self):
        self.assertTrue(isnan(negotiated_formula.backfat))

    def test_loin_depth(self):
        self.assertTrue(isnan(negotiated_formula.loin_depth))

    def test_loineye_area(self):
        self.assertTrue(isnan(negotiated_formula.loineye_area))

    def test_lean_percent(self):
        self.assertTrue(isnan(negotiated_formula.lean_percent))


class TestRecordArray(TestCase):
    def test_length(self):
        self.assertEqual(len(records), 2)

    def test_index(self):
        self.assertTrue(all(records.date == date(2019, 2, 1)))
