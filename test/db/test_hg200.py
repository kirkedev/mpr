from unittest import TestCase
from datetime import date

from numpy import isclose
from numpy import isnan

from mpr.data import db
from mpr.data.api.purchase import parse_attributes
from mpr.data.model.purchase import to_array
from mpr.data.model.purchase_type import Seller, Arrangement, Basis


class TestHg200(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = db.get('lm_hg200').barrows_gilts

    def test_create(self):
        self.assertTrue('/mpr/lm_hg200' in db.connection)
        self.assertTrue('/mpr/lm_hg200/barrows_gilts' in db.connection)
        self.assertTrue(self.report.table.will_query_use_indexing("""date == observation_date""", {
            'observation_date': date.toordinal(date(2019, 2, 1))
        }))

    @classmethod
    def tearDownClass(cls):
        db.connection.remove_node('/mpr/lm_hg200/barrows_gilts')
        db.connection.remove_node('/mpr/lm_hg200')

    def setUp(self):
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
        assert self.report.table.nrows == 2

    def tearDown(self):
        self.report.table.remove_rows()

    def test_query(self):
        result = self.report.query("""arrangement == negotiated""", {
            'negotiated': Arrangement.NEGOTIATED
        })

        negotiated = next(result)
        self.assertEqual(negotiated.date, date(2018, 1, 1))
        self.assertEqual(negotiated.seller, Seller.ALL)
        self.assertEqual(negotiated.arrangement, Arrangement.NEGOTIATED)
        self.assertEqual(negotiated.basis, Basis.CARCASS)
        self.assertEqual(negotiated.head_count, 11234)
        self.assertTrue(isclose(negotiated.low_price, 48.00))
        self.assertTrue(isclose(negotiated.high_price, 51.75))
        self.assertTrue(isclose(negotiated.avg_price, 50.70))

    def test_array(self):
        records = to_array(self.report.get())
        self.assertEqual(len(records), 2)
        self.assertTrue(all(records.date == date(2018, 1, 1)))
        self.assertTrue(len(records.arrangement == Arrangement.NEGOTIATED), 1)
        self.assertTrue(len(records.arrangement == Arrangement.NEGOTIATED_FORMULA), 1)

        result = records[records.arrangement == Arrangement.NEGOTIATED_FORMULA]
        negotiated_formula = result[0]
        self.assertEqual(negotiated_formula.head_count, 165)
        self.assertTrue(isnan(negotiated_formula.low_price))
        self.assertTrue(isnan(negotiated_formula.high_price))
        self.assertTrue(isnan(negotiated_formula.avg_price))

    def test_index(self):
        purchase = parse_attributes({
            'reported_for_date': '1/2/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '14141',
            'price_low': '48.00',
            'price_high': '52.00',
            'wtd_avg': '50.00'
        })

        self.report.insert([purchase])
        date_column = self.report.table.cols.date
        date_index = self.report.table.colindexes['date']
        self.assertEqual(date_column[date_index[0]], date(2018, 1, 1).toordinal())
        self.assertEqual(date_column[date_index[-1]], date(2018, 1, 2).toordinal())

    def test_merge(self):
        purchases = (parse_attributes({
            'reported_for_date': '1/1/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '11,234',
            'price_low': '48.00',
            'price_high': '51.75',
            'wtd_avg': '50.70'
        }), parse_attributes({
            'reported_for_date': '1/2/2018',
            'purchase_type': 'Negotiated (carcass basis)',
            'head_count': '10,000',
            'price_low': '48.00',
            'price_high': '52.00',
            'wtd_avg': '50.00'
        }))

        self.report.insert(purchases)
        self.assertEqual(self.report.table.nrows, 3)
