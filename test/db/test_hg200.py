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
        cls.report = barrows_gilts

    def test_create(self):
        self.assertTrue('/mpr/lm_hg200' in db.connection)
        self.assertTrue('/mpr/lm_hg200/barrows_gilts' in db.connection)

    @classmethod
    def tearDownClass(cls):
        db.connection.remove_node('/mpr/lm_hg200/barrows_gilts')
        db.connection.remove_node('/mpr/lm_hg200')

    def tearDown(self):
        self.report.table.remove_rows()

    def test_insert(self):
        purchase = parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '11,234',
            'price_low': '48.00',
            'price_high': '51.75',
            'wtd_avg': '50.70'
        })

        self.report.insert([purchase])

        data = next(self.report.get())
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

        self.report.insert([purchase])

        data = next(self.report.get())
        self.assertEqual(data.date, date(2018, 1, 1))
        self.assertEqual(data.arrangement, Arrangement.NEGOTIATED_FORMULA)
        self.assertEqual(data.head_count, 165)
        self.assertTrue(isnan(data.low_price))
        self.assertTrue(isnan(data.high_price))
        self.assertTrue(isnan(data.avg_price))

    def test_insert_multiple(self):
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

        self.report.insert(purchases)
        self.assertEqual(self.report.table.nrows, 2)

    def test_recarray(self):
        purchases = parse_attributes({
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
        })

        self.report.insert(purchases)
        self.report.commit()

        records = to_array(self.report.get())
        self.assertEqual(len(records), 2)
        self.assertTrue(all(records.date == date(2018, 1, 1)))
        self.assertTrue(all(records.seller == Seller.ALL))
        self.assertTrue(all(records.basis == Basis.CARCASS))
        self.assertTrue(len(records.arrangement == Arrangement.NEGOTIATED), 1)
        self.assertTrue(len(records.arrangement == Arrangement.NEGOTIATED_FORMULA), 1)
