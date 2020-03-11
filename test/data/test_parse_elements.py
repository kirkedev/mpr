from numpy import isnan
from numpy import isclose

from mpr.data import opt_int
from mpr.data import opt_float

from test import load_resource


def test_parse_int():
    attr = {'volume': '1,234'}
    assert opt_int(attr, 'volume') == 1234


def test_parse_float():
    attr = {'weight': '1,234.56'}
    assert isclose(opt_float(attr, 'weight'), 1234.56)


def test_opt_int():
    assert opt_int({}, 'volume') == 0
    assert opt_int({'volume': 'null'}, 'volume') == 0


def test_opt_float():
    assert isnan(opt_float({}, 'volume'))
    assert isnan(opt_float({'weight': 'null'}, 'volume'))


def test_parse_elements():
    records = load_resource('cutout.xml')

    cutout = next(records)
    assert cutout['slug'] == 'LM_PK602'
    assert cutout['report_date'] == '02/27/2019'
    assert cutout['label'] == 'Cutout and Primal Values'
    assert cutout['pork_carcass'] == '59.57'
    assert cutout['pork_loin'] == '57.98'
    assert cutout['pork_butt'] == '66.48'
    assert cutout['pork_picnic'] == '34.76'
    assert cutout['pork_rib'] == '110.69'
    assert cutout['pork_ham'] == '45.24'
    assert cutout['pork_belly'] == '97.67'

    volume = next(records)
    assert volume['slug'] == 'LM_PK602'
    assert volume['report_date'] == '02/27/2019'
    assert volume['label'] == 'Current Volume'
    assert volume['temp_cuts_total_load'] == '312.00'
    assert volume['temp_process_total_load'] == '41.31'

    bacon = next(records)
    assert bacon['slug'] == 'LM_PK602'
    assert bacon['report_date'] == '02/27/2019'
    assert bacon['label'] == 'Belly Cuts'
    assert bacon['Item_Description'] == 'Derind Belly 13-17#'
    assert bacon['total_pounds'] == '320,000'
    assert bacon['price_range_low'] == '112.94'
    assert bacon['price_range_high'] == '130.63'
    assert bacon['weighted_average'] == '119.57'
