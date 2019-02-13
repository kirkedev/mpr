from unittest import TestCase
from datetime import date

from test.api import load_resource
from mpr.data.api.purchase import parse_attributes

records = list(load_resource('test/api/resources/purchase.xml'))
assert len(records) == 7

negotiated = parse_attributes(records[0])
negotiated_formula = parse_attributes(records[1])


class NegotiatedPurchaseTest(TestCase):
    def test_report_date(self):
        self.assertEqual(negotiated.date, date(2019, 1, 31))

    def test_purchase_type(self):
        self.assertEqual(negotiated.purchase_type, 'Negotiated (carcass basis)')

    def test_head_count(self):
        self.assertEqual(negotiated.head_count, 11325)

    def test_avg_price(self):
        self.assertEqual(negotiated.avg_price, 50.7)

    def test_low_price(self):
        self.assertEqual(negotiated.low_price, 48.0)

    def test_high_price(self):
        self.assertEqual(negotiated.high_price, 51.75)


class NegotiatedFormulaTest(TestCase):
    def test_report_date(self):
        self.assertEqual(negotiated_formula.date, date(2019, 1, 31))

    def test_purchase_type(self):
        self.assertEqual(negotiated_formula.purchase_type, 'Negotiated Formula (carcass basis)')

    def test_head_count(self):
        self.assertEqual(negotiated_formula.head_count, 165)

    def test_avg_price(self):
        self.assertEqual(negotiated_formula.avg_price, None)

    def test_low_price(self):
        self.assertEqual(negotiated_formula.low_price, None)

    def test_high_price(self):
        self.assertEqual(negotiated_formula.high_price, None)
