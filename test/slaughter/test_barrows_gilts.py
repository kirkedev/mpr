import json
from datetime import date
from numpy import isnan
from numpy import isclose

from mpr.slaughter.api import parse_attributes
from mpr.slaughter.model import to_array
from mpr.purchase_type import Seller, Arrangement, Basis

with open('test/resources/slaughter.json') as resource:
    barrows_gilts = json.load(resource)
    assert len(barrows_gilts) == 8

negotiated = parse_attributes(barrows_gilts[0])
other_market_formula = parse_attributes(barrows_gilts[1])
market_formula = parse_attributes(barrows_gilts[2])
other_purchase = parse_attributes(barrows_gilts[3])
negotiated_formula = parse_attributes(barrows_gilts[4])
packer_owned = parse_attributes(barrows_gilts[7])


def test_negotiated():
    assert negotiated.date == date(2019, 2, 1)
    assert negotiated.report_date == date(2019, 2, 4)
    assert negotiated.seller == Seller.PRODUCER
    assert negotiated.arrangement == Arrangement.NEGOTIATED
    assert negotiated.basis == Basis.ALL
    assert isclose(negotiated.head_count, 12_771)
    assert isclose(negotiated.base_price, 51.8)
    assert isclose(negotiated.net_price, 53.26)
    assert isclose(negotiated.low_price, 43.57)
    assert isclose(negotiated.high_price, 57.85)
    assert isclose(negotiated.live_weight, 273.54)
    assert isclose(negotiated.carcass_weight, 205.41)
    assert isclose(negotiated.sort_loss, -2.16)
    assert isclose(negotiated.backfat, 0.61)
    assert isclose(negotiated.loin_depth, 2.61)
    assert isclose(negotiated.loineye_area, 7.83)
    assert isclose(negotiated.lean_percent, 55.60)
    assert isclose(negotiated.total_weight, 2_623_291.16)
    assert isclose(negotiated.total_value, 13_9716_484.52)
    assert isclose(negotiated.avg_price, 53.26)


def test_other_market_formula():
    assert other_market_formula.date == date(2019, 2, 1)
    assert other_market_formula.report_date == date(2019, 2, 4)
    assert other_market_formula.seller == Seller.PRODUCER
    assert other_market_formula.arrangement == Arrangement.OTHER_MARKET_FORMULA
    assert other_market_formula.basis == Basis.ALL
    assert other_market_formula.head_count == 71_962
    assert isclose(other_market_formula.base_price, 56.81)
    assert isclose(other_market_formula.net_price, 59.14)
    assert isclose(other_market_formula.low_price, 47.51)
    assert isclose(other_market_formula.high_price, 69.91)
    assert isclose(other_market_formula.live_weight, 288.18)
    assert isclose(other_market_formula.carcass_weight, 218.50)
    assert isclose(other_market_formula.sort_loss, -2.14)
    assert isclose(other_market_formula.backfat, 0.61)
    assert isclose(other_market_formula.loin_depth, 2.73)
    assert isclose(other_market_formula.loineye_area, 8.23)
    assert isclose(other_market_formula.lean_percent, 56.29)
    assert isclose(other_market_formula.total_weight, 15_723_697)
    assert isclose(other_market_formula.total_value, 929_899_440.58)
    assert isclose(other_market_formula.avg_price, 59.14)


def test_swine_pork_market_formula():
    assert market_formula.date == date(2019, 2, 1)
    assert market_formula.report_date == date(2019, 2, 4)
    assert market_formula.seller == Seller.PRODUCER
    assert market_formula.arrangement == Arrangement.MARKET_FORMULA
    assert market_formula.basis == Basis.ALL
    assert market_formula.head_count == 256_439
    assert isclose(market_formula.base_price, 55.53)
    assert isclose(market_formula.net_price, 57.65)
    assert isclose(market_formula.low_price, 37.89)
    assert isclose(market_formula.high_price, 67.65)
    assert isclose(market_formula.live_weight, 286.91)
    assert isclose(market_formula.carcass_weight, 216.06)
    assert isclose(market_formula.sort_loss, -1.85)
    assert isclose(market_formula.backfat, 0.64)
    assert isclose(market_formula.loin_depth, 2.65)
    assert isclose(market_formula.loineye_area, 7.97)
    assert isclose(market_formula.lean_percent, 56.00)
    assert isclose(market_formula.total_weight, 55_406_210.34)
    assert isclose(market_formula.total_value, 3_194_168_026.10)
    assert isclose(market_formula.avg_price, 57.65)


def test_other_purchase_agreement():
    assert other_purchase.date == date(2019, 2, 1)
    assert other_purchase.report_date == date(2019, 2, 4)
    assert other_purchase.seller == Seller.PRODUCER
    assert other_purchase.arrangement == Arrangement.OTHER_PURCHASE
    assert other_purchase.basis == Basis.ALL
    assert other_purchase.head_count == 134_335
    assert isclose(other_purchase.base_price, 63.31)
    assert isclose(other_purchase.net_price, 64.15)
    assert isclose(other_purchase.low_price, 47.39)
    assert isclose(other_purchase.high_price, 77.44)
    assert isclose(other_purchase.live_weight, 284.97)
    assert isclose(other_purchase.carcass_weight, 213.73)
    assert isclose(other_purchase.sort_loss, -1.51)
    assert isclose(other_purchase.backfat, 0.71)
    assert isclose(other_purchase.loin_depth, 2.49)
    assert isclose(other_purchase.loineye_area, 7.48)
    assert isclose(other_purchase.lean_percent, 55.18)
    assert isclose(other_purchase.total_weight, 28_711_419.55)
    assert isclose(other_purchase.total_value, 1_841_837_564.13)
    assert isclose(other_purchase.avg_price, 64.15)


def test_negotiated_formula():
    assert negotiated_formula.date == date(2019, 2, 1)
    assert negotiated_formula.report_date == date(2019, 2, 4)
    assert negotiated_formula.arrangement == Arrangement.NEGOTIATED_FORMULA
    assert negotiated_formula.basis == Basis.ALL
    assert negotiated_formula.head_count == 683
    assert isnan(negotiated_formula.base_price)
    assert isnan(negotiated_formula.net_price)
    assert isnan(negotiated_formula.low_price)
    assert isnan(negotiated_formula.high_price)
    assert isnan(negotiated_formula.live_weight)
    assert isnan(negotiated_formula.carcass_weight)
    assert isnan(negotiated_formula.sort_loss)
    assert isnan(negotiated_formula.backfat)
    assert isnan(negotiated_formula.loin_depth)
    assert isnan(negotiated_formula.loineye_area)
    assert isnan(negotiated_formula.lean_percent)
    assert isnan(negotiated_formula.total_weight)
    assert isnan(negotiated_formula.total_value)
    assert isnan(negotiated_formula.avg_price)


def test_packer_owned():
    assert packer_owned.date == date(2019, 2, 1)
    assert packer_owned.report_date == date(2019, 2, 4)
    assert packer_owned.arrangement == Arrangement.PACKER_OWNED
    assert packer_owned.basis == Basis.ALL
    assert packer_owned.head_count == 252_211
    assert isnan(packer_owned.base_price)
    assert isnan(packer_owned.net_price)
    assert isnan(packer_owned.low_price)
    assert isnan(packer_owned.high_price)
    assert isclose(packer_owned.live_weight, 287.07)
    assert isclose(packer_owned.carcass_weight, 218.47)
    assert isnan(packer_owned.sort_loss)
    assert isclose(packer_owned.backfat, 0.67)
    assert isclose(packer_owned.loin_depth, 2.52)
    assert isclose(packer_owned.loineye_area, 7.57)
    assert isclose(packer_owned.lean_percent, 54.11)
    assert isclose(packer_owned.total_weight, 55_100_537.17)
    assert isnan(packer_owned.total_value)
    assert isnan(packer_owned.avg_price)


def test_record_array():
    records = to_array([
        negotiated,
        other_market_formula,
        market_formula,
        negotiated_formula,
        packer_owned
    ])

    assert len(records) == 5
    assert all(records.date == date(2019, 2, 1))
