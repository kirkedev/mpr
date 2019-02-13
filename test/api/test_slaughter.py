from unittest import TestCase
from datetime import date

from test.api import load_resource
from mpr.data.api.slaughter import parse_attributes

records = list(load_resource('test/api/resources/slaughter.xml'))
assert len(records) == 8

negotiated = parse_attributes(records[0])
negotiated_formula = parse_attributes(records[4])


class NegotiatedPurchaseTest(TestCase):
    def test_date(self):
        self.assertEqual(negotiated.date, date(2019, 2, 1))

    def test_purchase_type(self):
        self.assertEqual(negotiated.purchase_type, 'Prod. Sold Negotiated')

    def test_head_count(self):
        self.assertEqual(negotiated.head_count, 12771)

    def test_base_price(self):
        self.assertEqual(negotiated.base_price, 51.8)

    def test_net_price(self):
        self.assertEqual(negotiated.net_price, 53.26)

    def test_low_price(self):
        self.assertEqual(negotiated.low_price, 43.57)

    def test_high_price(self):
        self.assertEqual(negotiated.high_price, 57.85)

    def test_live_weight(self):
        self.assertEqual(negotiated.live_weight, 273.54)

    def test_carcass_weight(self):
        self.assertEqual(negotiated.carcass_weight, 205.41)

    def test_sort_loss(self):
        self.assertEqual(negotiated.sort_loss, -2.16)

    def test_backfat(self):
        self.assertEqual(negotiated.backfat, 0.61)

    def test_loin_depth(self):
        self.assertEqual(negotiated.loin_depth, 2.61)

    def test_loineye_area(self):
        self.assertEqual(negotiated.loineye_area, 7.83)

    def test_lean_percent(self):
        self.assertEqual(negotiated.lean_percent, 55.6)


class NegotiatedFormulaTest(TestCase):
    def test_date(self):
        self.assertEqual(negotiated_formula.date, date(2019, 2, 1))

    def test_purchase_type(self):
        self.assertEqual(negotiated_formula.purchase_type, 'Prod. Sold Negotiated Formula')

    def test_head_count(self):
        self.assertEqual(negotiated_formula.head_count, 683)

    def test_base_price(self):
        self.assertEqual(negotiated_formula.base_price, None)

    def test_net_price(self):
        self.assertEqual(negotiated_formula.net_price, None)

    def test_low_price(self):
        self.assertEqual(negotiated_formula.low_price, None)

    def test_high_price(self):
        self.assertEqual(negotiated_formula.high_price, None)

    def test_live_weight(self):
        self.assertEqual(negotiated_formula.live_weight, None)

    def test_carcass_weight(self):
        self.assertEqual(negotiated_formula.carcass_weight, None)

    def test_sort_loss(self):
        self.assertEqual(negotiated_formula.sort_loss, None)

    def test_backfat(self):
        self.assertEqual(negotiated_formula.backfat, None)

    def test_loin_depth(self):
        self.assertEqual(negotiated_formula.loin_depth, None)

    def test_loineye_area(self):
        self.assertEqual(negotiated_formula.loineye_area, None)

    def test_lean_percent(self):
        self.assertEqual(negotiated_formula.lean_percent, None)
