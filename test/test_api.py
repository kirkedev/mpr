from numpy import isnan
from numpy import isclose

from mpr.api import filter_sections
from mpr.api import opt_int
from mpr.api import opt_float
from mpr.reports import CutoutSection

from test import load_resource

elements = load_resource('api/cutout.xml')
records = filter_sections(elements, CutoutSection.CUTOUT, CutoutSection.VOLUME)


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


def test_parse_attributes():
    cutout, volume = next(records)

    assert volume['slug'] == 'LM_PK603'
    assert volume['report_date'] == '08/20/2018'
    assert volume['label'] == 'Current Volume'
    assert volume['temp_cuts_total_load'] == '334.74'
    assert volume['temp_process_total_load'] == '39.61'

    assert cutout['slug'] == 'LM_PK603'
    assert cutout['report_date'] == '08/20/2018'
    assert cutout['label'] == 'Cutout and Primal Values'
    assert cutout['pork_carcass'] == '67.18'
    assert cutout['pork_loin'] == '75.51'
    assert cutout['pork_butt'] == '89.55'
    assert cutout['pork_picnic'] == '41.82'
    assert cutout['pork_rib'] == '113.95'
    assert cutout['pork_ham'] == '57.52'
    assert cutout['pork_belly'] == '77.77'
