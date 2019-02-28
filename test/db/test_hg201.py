from unittest import TestCase
from datetime import date

from numpy import isclose
from numpy import isnan

from mpr.data import db
from mpr.data.api.slaughter import parse_attributes
from mpr.data.model.slaughter import to_array
from mpr.data.model.purchase_type import Seller, Arrangement, Basis


class TestHg201(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = db.get('lm_hg201', 'barrows_gilts')

    def test_create(self):
        self.assertTrue('/mpr/lm_hg201' in db.connection)
        self.assertTrue('/mpr/lm_hg201/barrows_gilts' in db.connection)
        self.assertTrue(self.report.table.will_query_use_indexing("""date == observation_date""", {
            'observation_date': date.toordinal(date(2019, 2, 1))
        }))

    @classmethod
    def tearDownClass(cls):
        db.connection.remove_node('/mpr/lm_hg201/barrows_gilts')
        db.connection.remove_node('/mpr/lm_hg201')

    def setUp(self):
        records = (parse_attributes({
            'for_date_begin': '02/01/2019',
            'report_date': '02/04/2019',
            'purchase_type': 'Prod. Sold Negotiated',
            'head_count': '12,771',
            'base_price': '51.80',
            'avg_net_price': '53.26',
            'lowest_net_price': '43.57',
            'highest_net_price': '57.85',
            'avg_live_weight': '273.54',
            'avg_carcass_weight': '205.41',
            'avg_sort_loss': '-2.16',
            'avg_lean_percent': '55.60',
            'avg_backfat': '.61',
            'avg_loin_depth': '2.61',
            'loineye_area': '7.83'
        }), parse_attributes({
            'for_date_begin': '02/01/2019',
            'report_date': '02/04/2019',
            'purchase_type': 'Prod. Sold Negotiated Formula',
            'head_count': '683'
        }))

        self.report.insert(records)
        assert self.report.table.nrows == 2

    def tearDown(self):
        self.report.table.remove_rows()

    def test_query(self):
        record = next(self.report.get())
        self.assertEqual(record.date, date(2019, 2, 1))
        self.assertEqual(record.report_date, date(2019, 2, 4))
        self.assertEqual(record.seller, Seller.PRODUCER)
        self.assertEqual(record.arrangement, Arrangement.NEGOTIATED)
        self.assertEqual(record.basis, Basis.ALL)
        self.assertEqual(record.head_count, 12771)
        self.assertTrue(isclose(record.base_price, 51.80))
        self.assertTrue(isclose(record.net_price, 53.26))
        self.assertTrue(isclose(record.low_price, 43.57))
        self.assertTrue(isclose(record.high_price, 57.85))
        self.assertTrue(isclose(record.live_weight, 273.54))
        self.assertTrue(isclose(record.carcass_weight, 205.41))
        self.assertTrue(isclose(record.sort_loss, -2.16))
        self.assertTrue(isclose(record.lean_percent, 55.60))
        self.assertTrue(isclose(record.backfat, 0.61))
        self.assertTrue(isclose(record.loin_depth, 2.61))
        self.assertTrue(isclose(record.loineye_area, 7.83))

    def test_array(self):
        records = to_array(self.report.get_date(date(2019, 2, 1)))
        self.assertEqual(len(records), 2)
        self.assertTrue(all(records.date == date(2019, 2, 1)))
        self.assertTrue(all(records.report_date == date(2019, 2, 4)))
        self.assertTrue(len(records.arrangement == Arrangement.NEGOTIATED), 1)
        self.assertTrue(len(records.arrangement == Arrangement.NEGOTIATED_FORMULA), 1)

        result = records[records.arrangement == Arrangement.NEGOTIATED_FORMULA]
        record = result[0]
        self.assertEqual(record.head_count, 683)
        self.assertTrue(isnan(record.base_price))
        self.assertTrue(isnan(record.net_price))
        self.assertTrue(isnan(record.low_price))
        self.assertTrue(isnan(record.high_price))
        self.assertTrue(isnan(record.live_weight))
        self.assertTrue(isnan(record.carcass_weight))
        self.assertTrue(isnan(record.sort_loss, ))
        self.assertTrue(isnan(record.lean_percent))
        self.assertTrue(isnan(record.backfat))
        self.assertTrue(isnan(record.loin_depth))
        self.assertTrue(isnan(record.loineye_area))
