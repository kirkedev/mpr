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


class CashIndexTest(TestCase):
    # Cash prices for Feb 18-19, 2019
    # ftp://ftp.cmegroup.com/cash_settled_commodity_index_prices/daily_data/lean_hogs/LH190219.txt

    def test_latest_weighted_price(self):
        latest = purchase_types[purchase_types.date == date(2019, 2, 19)]
        weights = total_weight(latest.head_count, latest.carcass_weight)
        values = total_value(weights, latest.net_price)
        prices = avg_price(np.nansum(values), np.nansum(weights))
        price = np.round(prices, decimals=2)
        self.assertTrue(np.isclose(price, 54.19))

    def test_prior_day_weighted_price(self):
        yesterday = purchase_types[purchase_types.date == date(2019, 2, 18)]
        weights = total_weight(yesterday.head_count, yesterday.carcass_weight)
        values = total_value(weights, yesterday.net_price)
        prices = avg_price(np.nansum(values), np.nansum(weights))
        price = np.round(prices, decimals=2)
        self.assertTrue(np.isclose(price, 54.08))
