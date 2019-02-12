from unittest import TestCase
from xml.etree import ElementTree
from io import StringIO

from mpr.data.api import Attributes
from mpr.data.api import opt_int
from mpr.data.api import opt_float
from mpr.data.api import parse_elements
from mpr.data.api import filter_sections

from test.api import load_resource

elements = load_resource('test/api/resources/cutout.xml')
records = filter_sections(elements, 'Cutout and Primal Values', 'Current Volume')
volume, cutout = next(records)

class ParseReportTest(TestCase):
    def test_parse_int(self):
        attr = {'volume': '1,234'}
        self.assertEqual(opt_int(attr, 'volume'), 1234)

    def test_opt_int(self):
        attr = {'volume': 'null'}
        self.assertEqual(opt_int(attr, 'volume'), None)

    def test_parse_float(self):
        attr = {'weight': '1,234.56'}
        self.assertEqual(opt_float(attr, 'weight'), 1234.56)

    def test_opt_float(self):
        attr = {'volume': 'null'}
        self.assertEqual(opt_float(attr, 'volume'), None)

    def test_volume_datel(self):
        self.assertEqual(volume['report_date'], '08/20/2018')

    def test_volume_label(self):
        self.assertEqual(volume['label'], 'Current Volume')
    
    def test_primal_loads(self):
        self.assertEqual(volume['temp_cuts_total_load'], '334.74')
    
    def test_trimming_loads(self):
        self.assertEqual(volume['temp_process_total_load'], '39.61')

    def test_cutout_date(self):
        self.assertEqual(cutout['report_date'], '08/20/2018')

    def test_cutout_label(self):
        self.assertEqual(cutout['label'], 'Cutout and Primal Values')

    def test_carcass_value(self):
        self.assertEqual(cutout['pork_carcass'], '67.18')

    def test_loin_value(self):
        self.assertEqual(cutout['pork_loin'], '75.51')

    def test_butt_value(self):
        self.assertEqual(cutout['pork_butt'], '89.55')

    def test_picnic_value(self):
        self.assertEqual(cutout['pork_picnic'], '41.82')

    def test_rib_value(self):
        self.assertEqual(cutout['pork_rib'], '113.95')

    def test_ham_value(self):
        self.assertEqual(cutout['pork_ham'], '57.52')

    def test_belly_value(self):
        self.assertEqual(cutout['pork_belly'], '77.77')
