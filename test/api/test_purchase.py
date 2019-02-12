from unittest import TestCase
from datetime import date

from test.api import parse_report
from mpr.data.api.purchase import parse_attributes

report = """
    <results exportTime="2019-02-11 20:50:38">
        <report label="National Daily Direct Hog Prior Day - Purchased Swine" slug="LM_HG200">
            <record report_date="02/01/2019" reported_for_date="01/31/2019">
                <report label="Barrows/Gilts (producer/packer sold)">
                    <record purchase_type="Negotiated (carcass basis)" head_count="11,325" price_low="48.00" price_high="51.75" wtd_avg="50.70" rolling_avg="51.26"/>
                    <record purchase_type="Negotiated Formula (carcass basis)" head_count="165"/>
                    <record purchase_type="Combined Negotiated/Negotiated Formula (carcass basis)" head_count="11,490"/>
                    <record purchase_type="Swine/Pork Market Formula (carcass basis)" head_count="139,569" price_low="48.88" price_high="63.83" wtd_avg="55.40"/>
                    <record purchase_type="Negotiated (live basis)" head_count="703" price_low="34.00" price_high="41.75" wtd_avg="39.92" rolling_avg="40.14"/>
                    <record purchase_type="Negotiated Formula (live basis)" head_count="0"/>
                    <record purchase_type="Combined Negotiated/Negotiated Formula (live basis)" head_count="703"/>
                </report>
            </record>
        </report>
    </results>
"""

records = list(parse_report(report))
attributes = records[0]
negotiated = parse_attributes(attributes)

class PurchaseTest(TestCase):
    def test_parse_length(self):
        self.assertEqual(len(records), 7)
    
    def test_report_date(self):
        self.assertEqual(negotiated.date, date(2019, 1, 31))
    
    def test_purchase_type(self):
        self.assertEqual(negotiated.purchase_type, 'Negotiated (carcass basis)')

    def test_head_count(self):
        self.assertEqual(negotiated.head_count, 11325)
    
    def test_avg_price(self):
        self.assertEqual(negotiated.avg_price, 50.7)
    
    def test_low_price(self):
        self.assertEqual(negotiated.low_price, 48.0)
    
    def test_high_price(self):
        self.assertEqual(negotiated.high_price, 51.75)
