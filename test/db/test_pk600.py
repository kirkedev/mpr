from unittest import TestCase
from datetime import date
from numpy import isclose

from mpr.data import db
from mpr.data.api.cutout import parse_attributes
from mpr.data.model.cutout import to_array


class TestPk600(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = db.get('lm_pk600').cutout

    def test_create(self):
        self.assertTrue('/mpr/lm_pk600' in db.connection)
        self.assertTrue('/mpr/lm_pk600/cutout' in db.connection)
        self.assertTrue(self.report.table.will_query_use_indexing("""date == observation_date""", {
            'observation_date': date.toordinal(date(2019, 2, 1))
        }))

    @classmethod
    def tearDownClass(cls):
        db.connection.remove_node('/mpr/lm_pk600/cutout')
        db.connection.remove_node('/mpr/lm_pk600')

    def setUp(self):
        cutout = (parse_attributes({
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        }, {
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }), parse_attributes({
            'report_date': '08/21/2018',
            'temp_cuts_total_load': '396.3',
            'temp_process_total_load': '52.57'
        }, {
            'pork_carcass': '66.19',
            'pork_loin': '74.05',
            'pork_butt': '90.15',
            'pork_picnic': '40.61',
            'pork_rib': '115.35',
            'pork_ham': '55.92',
            'pork_belly': '76.45'
        }))

        self.report.insert(cutout)
        assert self.report.table.nrows == 2

    def tearDown(self):
        self.report.table.remove_rows()

    def test_query(self):
        result = self.report.get_range(start=date(2018, 8, 1), end=date(2018, 8, 20))
        records = list(result)
        self.assertEqual(len(records), 1)

        record = records[0]
        self.assertEqual(record.date, date(2018, 8, 20))
        self.assertEqual(record.report_date, date(2018, 8, 20))
        self.assertTrue(isclose(record.primal_loads, 334.74))
        self.assertTrue(isclose(record.trimming_loads, 39.61))
        self.assertTrue(isclose(record.carcass_price, 67.18))
        self.assertTrue(isclose(record.loin_price, 75.51))
        self.assertTrue(isclose(record.butt_price, 89.55))
        self.assertTrue(isclose(record.picnic_price, 41.82))
        self.assertTrue(isclose(record.rib_price, 113.95))
        self.assertTrue(isclose(record.ham_price, 57.52))
        self.assertTrue(isclose(record.belly_price, 77.77))

    def test_array(self):
        records = to_array(self.report.get())
        self.assertEqual(len(records), 2)

        result = records[records.date > date(2018, 8, 20)]
        self.assertEqual(len(result), 1)

        record = result[0]
        self.assertEqual(record.date, date(2018, 8, 21))
        self.assertEqual(record.report_date, date(2018, 8, 21))
        self.assertTrue(isclose(record.primal_loads, 396.3))
        self.assertTrue(isclose(record.trimming_loads, 52.57))
        self.assertTrue(isclose(record.carcass_price, 66.19))
        self.assertTrue(isclose(record.loin_price, 74.05))
        self.assertTrue(isclose(record.butt_price, 90.15))
        self.assertTrue(isclose(record.picnic_price, 40.61))
        self.assertTrue(isclose(record.rib_price, 115.35))
        self.assertTrue(isclose(record.ham_price, 55.92))
        self.assertTrue(isclose(record.belly_price, 76.45))

    def test_index(self):
        date_column = self.report.table.cols.date
        date_index = self.report.table.colindexes['date']
        self.assertEqual(date_column[date_index[0]], date(2018, 8, 20).toordinal())
        self.assertEqual(date_column[date_index[1]], date(2018, 8, 21).toordinal())
