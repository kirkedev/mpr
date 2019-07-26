from unittest import TestCase

from mpr.cutout.api import parse_attributes


class TestCutout(TestCase):
    def test_objects_are_the_same(self):
        first = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        })

        second = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '0.0',
            'pork_loin': '0.0',
            'pork_butt': '0.0',
            'pork_picnic': '0.0',
            'pork_rib': '0.0',
            'pork_ham': '0.0',
            'pork_belly': '0.0'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '0.0',
            'temp_process_total_load': '0.0'
        })

        self.assertEqual(hash(first), hash(second))

    def test_objects_are_not_the_same(self):
        first = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        })

        second = parse_attributes({
            'report_date': '08/21/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }, {
            'report_date': '08/21/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        })

        self.assertNotEqual(hash(first), hash(second))

    def test_contents_are_the_same(self):
        first = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        })

        second = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        })

        self.assertEqual(first, second)

    def test_contents_are_not_the_same(self):
        first = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        })

        second = parse_attributes({
            'report_date': '08/20/2018',
            'pork_carcass': '0.0',
            'pork_loin': '0.0',
            'pork_butt': '0.0',
            'pork_picnic': '0.0',
            'pork_rib': '0.0',
            'pork_ham': '0.0',
            'pork_belly': '0.0'
        }, {
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '0.0',
            'temp_process_total_load': '0.0'
        })

        self.assertNotEqual(first, second)
