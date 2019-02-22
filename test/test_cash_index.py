from unittest import TestCase
from datetime import date
import numpy as np
from mpr.data.api.slaughter import parse_attributes
from mpr.data.model.slaughter import to_array
from mpr.data.model.slaughter import total_weight
from mpr.data.model.slaughter import total_value
from mpr.data.model.slaughter import avg_price
from mpr.data.model.purchase_type import Arrangement

from . import load_resource

records = to_array(map(parse_attributes, load_resource('cash_prices.xml')))

negotiated = records.arrangement == Arrangement.NEGOTIATED
negotiated_formula = records.arrangement == Arrangement.NEGOTIATED_FORMULA
market_formula = records.arrangement == Arrangement.MARKET_FORMULA
purchase_types = records[negotiated | negotiated_formula | market_formula]

latest = purchase_types.date == date(2019, 2, 19)
prior_day = purchase_types.date == date(2019, 2, 18)


class CashIndexTest(TestCase):
    # Cash prices for Feb 18-19, 2019
    # ftp://ftp.cmegroup.com/cash_settled_commodity_index_prices/daily_data/lean_hogs/LH190219.txt

    def test_latest_weighted_price(self):
        latest_data = purchase_types[latest]
        weights = total_weight(latest_data.head_count, latest_data.carcass_weight)
        values = total_value(weights, latest_data.net_price)
        prices = avg_price(np.nansum(values), np.nansum(weights))
        price = np.round(prices, decimals=2)
        self.assertTrue(np.isclose(price, 54.19))

    def test_prior_day_weighted_price(self):
        prior_day_data = purchase_types[prior_day]
        weights = total_weight(prior_day_data.head_count, prior_day_data.carcass_weight)
        values = total_value(weights, prior_day_data.net_price)
        prices = avg_price(np.nansum(values), np.nansum(weights))
        price = np.round(prices, decimals=2)
        self.assertTrue(np.isclose(price, 54.08))

    def test_cme_lean_hog_index_price(self):
        data = purchase_types[latest | prior_day]
        weights = total_weight(data.head_count, data.carcass_weight)
        values = total_value(weights, data.net_price)
        prices = avg_price(np.nansum(values), np.nansum(weights))
        price = np.round(prices, decimals=2)
        self.assertTrue(np.isclose(price, 54.13))
