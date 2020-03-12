from datetime import datetime

from dateutil import utils
from dateutil.tz import tz

from mpr.cuts.report import lm_pk602
from mpr.cuts.report import lm_pk620


def test_report():
    assert str(lm_pk602) == 'lm_pk602'


def test_section():
    assert str(lm_pk602.Section.BELLY) == 'Belly Cuts'
    assert lm_pk602.Section.BELLY == 'Belly Cuts'

    sections = {'Belly Cuts': 123}
    assert sections[lm_pk602.Section.BELLY] == 123

    sections[lm_pk602.Section.BELLY] = 456
    assert sections['Belly Cuts'] == 456


def test_daily_yesterday(monkeypatch):
    def today(timezone: tz = None) -> datetime:
        return datetime(2019, 6, 20, 14, 55, tzinfo=timezone)

    monkeypatch.setattr(utils, 'today', today)

    latest = lm_pk602.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 19


def test_daily_today(monkeypatch):
    def today(timezone: tz = None) -> datetime:
        return datetime(2019, 6, 20, 15, 5, tzinfo=timezone)

    monkeypatch.setattr(utils, 'today', today)

    latest = lm_pk602.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 20


def test_daily_weekend(monkeypatch):
    def today(timezone: tz = None) -> datetime:
        return datetime(2019, 6, 16, 11, tzinfo=timezone)

    monkeypatch.setattr(utils, 'today', today)

    latest = lm_pk602.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 14


def test_weekly_before_release(monkeypatch):
    def today(timezone: tz = None) -> datetime:
        return datetime(2019, 6, 17, 9, 55, tzinfo=timezone)

    monkeypatch.setattr(utils, 'today', today)

    latest = lm_pk620.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 10


def test_weekly_after_release(monkeypatch):
    def today(timezone: tz = None) -> datetime:
        return datetime(2019, 6, 17, 10, 5, tzinfo=timezone)

    monkeypatch.setattr(utils, 'today', today)

    latest = lm_pk620.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 17
