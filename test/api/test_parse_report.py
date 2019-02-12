from unittest import TestCase
from xml.etree import ElementTree
from io import StringIO

from mpr.data.api import Attributes
from mpr.data.api import opt_int
from mpr.data.api import opt_float
from mpr.data.api import parse_elements

from test.api import load_report

report = """
    <results exportTime="2018-09-07 12:25:37 CDT">
        <report label="National Daily Pork Report - Negotiated Sales" slug="LM_PK603">
            <record report_date="08/20/2018">
                <report label="Cutout and Primal Values">
                    <record
                        pork_carcass="67.18"
                        pork_loin="75.51"
                        pork_butt="89.55"
                        pork_picnic="41.82"
                        pork_rib="113.95"
                        pork_ham="57.52"
                        pork_belly="77.77"/>
                </report>
            </record>
        </report>
    </results>
"""

elements = load_report(report)
records = parse_elements(elements)
attributes = next(records)

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

    def test_report_date(self):
        self.assertEqual(attributes['report_date'], '08/20/2018')

    def test_report_label(self):
        self.assertEqual(attributes['label'], 'Cutout and Primal Values')

    def test_carcass_value(self):
        self.assertEqual(attributes['pork_carcass'], '67.18')

    def test_loin_value(self):
        self.assertEqual(attributes['pork_loin'], '75.51')

    def test_butt_value(self):
        self.assertEqual(attributes['pork_butt'], '89.55')

    def test_picnic_value(self):
        self.assertEqual(attributes['pork_picnic'], '41.82')

    def test_rib_value(self):
        self.assertEqual(attributes['pork_rib'], '113.95')

    def test_ham_value(self):
        self.assertEqual(attributes['pork_ham'], '57.52')

    def test_belly_value(self):
        self.assertEqual(attributes['pork_belly'], '77.77')
