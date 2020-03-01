from datetime import date
import numpy as np

from mpr.slaughter.api import filter_section
from mpr.slaughter.api import parse_attributes
from mpr.slaughter.model import to_array
from mpr.purchase_type import Arrangement
from mpr.report import SlaughterReport

from test import load_resource

report = filter_section(load_resource('reports/cash_prices.xml'), SlaughterReport.Section.BARROWS_AND_GILTS)
records = to_array(map(parse_attributes, report))

negotiated = records.arrangement == Arrangement.NEGOTIATED
market_formula = records.arrangement == Arrangement.MARKET_FORMULA
negotiated_formula = records.arrangement == Arrangement.NEGOTIATED_FORMULA
purchase_types = records[negotiated | negotiated_formula | market_formula]


def weighted_avg_price(data: np.recarray) -> float:
    total_weights = data.head_count * data.carcass_weight
    total_values = data.net_price * total_weights
    prices = np.nansum(total_values) / np.nansum(total_weights)
    return np.round(prices, decimals=2)


def test_latest_weighted_price():
    data = purchase_types[purchase_types.date == date(2019, 2, 19)]
    assert np.isclose(weighted_avg_price(data), 54.19)


def test_prior_day_weighted_price():
    data = purchase_types[purchase_types.date == date(2019, 2, 18)]
    assert np.isclose(weighted_avg_price(data), 54.08)


def test_cme_lean_hog_index_price():
    latest = purchase_types.date == date(2019, 2, 19)
    prior_day = purchase_types.date == date(2019, 2, 18)
    data = purchase_types[latest | prior_day]
    assert np.isclose(weighted_avg_price(data), 54.13)
