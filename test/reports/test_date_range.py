from unittest import TestCase
from datetime import date
from datetime import datetime

from mpr.data.api import Attributes
from mpr.data.api import parse_elements
from xml.etree import ElementTree

from mpr.data import date_diff
from mpr.data import request_periods
from mpr.data.report_calendar import report_date_range


with open('test/resources/reports/report_dates.xml') as report:
    elements = ElementTree.iterparse(report, events=['start', 'end'])
    report_dates = parse_elements(elements, 1, 2)

    def parse_date(element: Attributes) -> date:
        report_date = element['report_date']
        return datetime.strptime(report_date, "%m/%d/%Y").date()

    calendar_dates = report_date_range(date(2001, 8, 6), date(2019, 2, 21))
    report_dates = map(parse_date, report_dates)

    # print('\n'.join(map(date.isoformat, sorted(date_diff(calendar_dates, report_dates)))))


class DateRangeTest(TestCase):
    def test_all_miss(self):
        dates = list(report_date_range(date(2019, 1, 15), date(2019, 1, 31)))
        intervals = request_periods(date(2019, 1, 1), date(2019, 1, 10), dates)
        self.assertEqual(intervals, [(date(2019, 1, 2), date(2019, 1, 10))])

    def test_all_hit(self):
        dates = report_date_range(date(2019, 1, 15), date(2019, 1, 31))
        intervals = request_periods(date(2019, 1, 15), date(2019, 1, 22), dates)
        self.assertEqual(len(intervals), 0)

    def test_half_hit(self):
        dates = report_date_range(date(2019, 1, 15), date(2019, 1, 31))
        intervals = request_periods(date(2019, 1, 1), date(2019, 1, 22), dates)
        self.assertEqual(intervals, [(date(2019, 1, 2), date(2019, 1, 14))])

    def test_hit_splits_range(self):
        dates = report_date_range(date(2019, 1, 15), date(2019, 1, 31))
        intervals = request_periods(date(2019, 1, 1), date(2019, 2, 28), dates)
        self.assertEqual(intervals, [(date(2019, 1, 2), date(2019, 1, 14)), (date(2019, 2, 1), date(2019, 2, 28))])
