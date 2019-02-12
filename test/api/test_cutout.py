from unittest import TestCase
from datetime import date

from test.api import parse_report
from mpr.data.api.cutout import parse_attributes

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
                <report label="Current Volume">
                    <record 
                        temp_cuts_total_load="334.74" 
                        temp_process_total_load="39.61"/>
                </report>
            </record>
        </report>
    </results>
"""

records = parse_report(report)
attributes = (next(records), next(records))
cutout = parse_attributes(attributes)

class CutoutTest(TestCase):
    def test_parse_date(self):
        self.assertEqual(cutout.date, date(2018, 8, 20))

    def test_primal_loads(self):
        self.assertEqual(cutout.primal_loads, 334.74)

    def test_trimming_loads(self):
        self.assertEqual(cutout.trimming_loads, 39.61)

    def test_parse_carcass_price(self):
        self.assertEqual(cutout.carcass_price, 67.18)

    def test_loin_price(self):
        self.assertEqual(cutout.loin_price, 75.51)

    def test_butt_price(self):
        self.assertEqual(cutout.butt_price, 89.55)
    
    def test_picnic_price(self):
        self.assertEqual(cutout.picnic_price, 41.82)
    
    def test_rib_price(self):
        self.assertEqual(cutout.rib_price, 113.95)

    def test_ham_price(self):
        self.assertEqual(cutout.ham_price, 57.52)
    
    def test_belly_price(self):
        self.assertEqual(cutout.belly_price, 77.77)
