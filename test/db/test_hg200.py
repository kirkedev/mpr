from unittest import TestCase
from datetime import date
from numpy import isclose
from numpy import isnan

from mpr.data import db
from mpr.data.api.purchase import parse_attributes
from mpr.data.model.purchase import to_array
from mpr.data.model.purchase_type import Seller
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.purchase_type import Basis


class TestHg200(TestCase):
    @classmethod
    def setUpClass(cls):
        from mpr.data.db.lm_hg200 import barrows_gilts
        cls.model = barrows_gilts

    def test_create(self):
        self.assertTrue('/mpr/lm_hg200' in db.connection)
        self.assertTrue('/mpr/lm_hg200/barrows_gilts' in db.connection)

    @classmethod
    def tearDownClass(cls):
        db.connection.remove_node('/mpr/lm_hg200/barrows_gilts')
        db.connection.remove_node('/mpr/lm_hg200')

    def tearDown(self):
        self.model.table.remove_rows()

    def test_insert(self):
        purchase = parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '11,234',
            'price_low': '48.00',
            'price_high': '51.75',
            'wtd_avg': '50.70'
        })

        self.model.append(purchase)
        self.model.commit()

        data = next(self.model.get())
        self.assertEqual(data.date, date(2018, 1, 1))
        self.assertEqual(data.seller, Seller.ALL)
        self.assertEqual(data.arrangement, Arrangement.NEGOTIATED)
        self.assertEqual(data.basis, Basis.CARCASS)
        self.assertEqual(data.head_count, 11234)
        self.assertTrue(isclose(data.low_price, 48.00))
        self.assertTrue(isclose(data.high_price, 51.75))
        self.assertTrue(isclose(data.avg_price, 50.70))

    def test_insert_with_nans(self):
        purchase = parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated Formula (carcass basis)',
            'head_count': '165'
        })

        self.model.append(purchase)
        self.model.commit()

        data = next(self.model.get())
        self.assertEqual(data.date, date(2018, 1, 1))
        self.assertEqual(data.arrangement, Arrangement.NEGOTIATED_FORMULA)
        self.assertEqual(data.head_count, 165)
        self.assertTrue(isnan(data.low_price))
        self.assertTrue(isnan(data.high_price))
        self.assertTrue(isnan(data.avg_price))

    def insert_multiple(self):
        purchases = (parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '11,234',
            'price_low': '48.00',
            'price_high': '51.75',
            'wtd_avg': '50.70'
        }), parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated Formula (carcass basis)',
            'head_count': '165'
        }))

        self.model.append_rows(purchases)

        data = self.model.get()
        self.assertEqual(len(list(data)), 2)

    def test_recarray(self):
        purchase = parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '11,234',
            'price_low': '48.00',
            'price_high': '51.75',
            'wtd_avg': '50.70'
        })

        self.model.append(purchase)
        self.model.commit()

        records = to_array(self.model.get())
        self.assertEqual(len(records), 1)
        self.assertTrue(all(records.date == date(2018, 1, 1)))
