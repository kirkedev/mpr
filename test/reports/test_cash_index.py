from unittest import TestCase
from datetime import date
import numpy as np

from mpr.data.api import filter_section
from mpr.data.api.slaughter import Section
from mpr.data.api.slaughter import parse_attributes
from mpr.data.model.slaughter import to_array
from mpr.data.model.purchase_type import Arrangement

from . import load_resource

report = filter_section(load_resource('cash_prices.xml'), Section.BARROWS_AND_GILTS.value)
records = to_array(map(parse_attributes, report))

negotiated = records.arrangement == Arrangement.NEGOTIATED
market_formula = records.arrangement == Arrangement.MARKET_FORMULA
negotiated_formula = records.arrangement == Arrangement.NEGOTIATED_FORMULA
purchase_types = records[negotiated | negotiated_formula | market_formula]


class TestCashIndex(TestCase):
    # Cash prices for Feb 18-19, 2019
    # ftp://ftp.cmegroup.com/cash_settled_commodity_index_prices/daily_data/lean_hogs/LH190219.txt
    @staticmethod
    def weighted_avg_price(data: np.recarray) -> float:
        total_weights = data.head_count * data.carcass_weight
        total_values = data.net_price * total_weights
        prices = np.nansum(total_values) / np.nansum(total_weights)
        return np.round(prices, decimals=2)

    def test_latest_weighted_price(self):
        data = purchase_types[purchase_types.date == date(2019, 2, 19)]
        price = self.weighted_avg_price(data)
        self.assertTrue(np.isclose(price, 54.19))

    def test_prior_day_weighted_price(self):
        data = purchase_types[purchase_types.date == date(2019, 2, 18)]
        price = self.weighted_avg_price(data)
        self.assertTrue(np.isclose(price, 54.08))

    def test_cme_lean_hog_index_price(self):
        latest = purchase_types.date == date(2019, 2, 19)
        prior_day = purchase_types.date == date(2019, 2, 18)
        data = purchase_types[latest | prior_day]
        price = self.weighted_avg_price(data)
        self.assertTrue(np.isclose(price, 54.13))
