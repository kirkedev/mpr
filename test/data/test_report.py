from datetime import date
from datetime import datetime
from datetime import time
from typing import Optional

from dateutil.tz import gettz

from mpr.data import report
from mpr.sales.report import lm_pk602
from mpr.sales.report import lm_pk620


def chicago_time(today: date, at: time):
    def get_time(hour: Optional[int] = None) -> datetime:
        result = datetime.combine(today, at, tzinfo=gettz('America/Chicago'))
        return result if hour is None else result.replace(hour=hour, minute=0, second=0, microsecond=0)

    return get_time


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
    monkeypatch.setattr(report, 'chicago_time', chicago_time(date(2019, 6, 20), time(14, 55)))

    latest = lm_pk602.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 19


def test_daily_today(monkeypatch):
    monkeypatch.setattr(report, 'chicago_time', chicago_time(date(2019, 6, 20), time(15, 5)))

    latest = lm_pk602.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 20


def test_daily_weekend(monkeypatch):
    monkeypatch.setattr(report, 'chicago_time', chicago_time(date(2019, 6, 16), time(11)))

    latest = lm_pk602.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 14


def test_weekly_before_release(monkeypatch):
    monkeypatch.setattr(report, 'chicago_time', chicago_time(date(2019, 6, 17), time(9, 55)))

    latest = lm_pk620.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 10


def test_weekly_after_release(monkeypatch):
    monkeypatch.setattr(report, 'chicago_time', chicago_time(date(2019, 6, 17), time(10, 5)))

    latest = lm_pk620.latest
    assert latest.year == 2019
    assert latest.month == 6
    assert latest.day == 17
