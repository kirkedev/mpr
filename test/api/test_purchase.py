from unittest import TestCase
from datetime import date
from numpy import isnan
from numpy import isclose

from mpr.data.api.purchase import parse_attributes
from mpr.data.model.purchase import to_array
from mpr.data.model.purchase_type import Seller, Arrangement, Basis

from test.api import load_resource

attributes = list(load_resource('purchase.xml'))
assert len(attributes) == 7

negotiated = parse_attributes(attributes[0])
negotiated_formula = parse_attributes(attributes[1])
records = to_array([negotiated, negotiated_formula])


class NegotiatedPurchaseTest(TestCase):
    def test_report_date(self):
        self.assertEqual(negotiated.date, date(2019, 1, 31))

    def test_seller(self):
        self.assertEqual(negotiated.seller, Seller.ALL)

    def test_arrangement(self):
        self.assertEqual(negotiated.arrangement, Arrangement.NEGOTIATED)

    def test_basis(self):
        self.assertEqual(negotiated.basis, Basis.CARCASS)

    def test_head_count(self):
        self.assertEqual(negotiated.head_count, 11325)

    def test_avg_price(self):
        self.assertTrue(isclose(negotiated.avg_price, 50.7))

    def test_low_price(self):
        self.assertTrue(isclose(negotiated.low_price, 48.0))

    def test_high_price(self):
        self.assertTrue(isclose(negotiated.high_price, 51.75))


class NegotiatedFormulaTest(TestCase):
    def test_report_date(self):
        self.assertEqual(negotiated_formula.date, date(2019, 1, 31))

    def test_arrangement(self):
        self.assertEqual(negotiated_formula.arrangement, Arrangement.NEGOTIATED_FORMULA)

    def test_head_count(self):
        self.assertEqual(negotiated_formula.head_count, 165)

    def test_avg_price(self):
        self.assertTrue(isnan(negotiated_formula.avg_price))

    def test_low_price(self):
        self.assertTrue(isnan(negotiated_formula.low_price))

    def test_high_price(self):
        self.assertTrue(isnan(negotiated_formula.high_price))


class TestRecordArray(TestCase):
    def test_length(self):
        self.assertEqual(len(records), 2)

    def test_index(self):
        self.assertTrue(all(records.date == date(2019, 1, 31)))
