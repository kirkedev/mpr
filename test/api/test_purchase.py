from unittest import TestCase
from datetime import date

from test.api import load_resource
from mpr.data.api.purchase import parse_attributes

records = list(load_resource('test/api/resources/purchase.xml'))
attributes = records[0]
negotiated = parse_attributes(attributes)


class PurchaseTest(TestCase):
    def test_parse_length(self):
        self.assertEqual(len(records), 7)

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
