import json
from datetime import date
from itertools import starmap

from numpy import isclose
from pytest import mark

from mpr.cutout import fetch_cutout
from mpr.cutout.api import parse_record
from mpr.cutout.model import to_array
from mpr.data.repository import Repository
from mpr.report import lm_pk602
from test.server import server

with open('test/resources/cutout.json') as resource:
    reports = json.load(resource)
    cutout = next(starmap(parse_record, zip(*reports)))


def test_parse_report():
    assert cutout.report == 'lm_pk602'
    assert cutout.date == date(2019, 2, 1)
    assert cutout.report_date == date(2019, 2, 1)
    assert isclose(cutout.primal_loads, 234.33)
    assert isclose(cutout.trimming_loads, 43.85)
    assert isclose(cutout.carcass_price, 66.99)
    assert isclose(cutout.loin_price, 67.85)
    assert isclose(cutout.butt_price, 73.05)
    assert isclose(cutout.picnic_price, 38.49)
    assert isclose(cutout.rib_price, 121.71)
    assert isclose(cutout.ham_price, 47.98)
    assert isclose(cutout.belly_price, 112.23)
    assert isclose(cutout.loads, 278.18)
    assert isclose(cutout.value, 18_635.28)


def test_record_array():
    records = to_array([cutout])
    assert len(records) == 1
    assert all(records.date == date(2019, 2, 1))
    assert all(records.report == 'lm_pk602')


@mark.asyncio
async def test_query():
    async with server():
        records = list(await fetch_cutout(lm_pk602, date(2019, 6, 1), date(2019, 6, 10)))

    assert len(records) == 6
