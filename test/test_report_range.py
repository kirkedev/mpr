from datetime import date
from unittest import TestCase

from mpr.report_range import ReportMonth, next_month, report_months, get_months, report_diff


class ReportRangeTest(TestCase):
    def test_equals(self):
        first = ReportMonth(2019, 1)
        second = ReportMonth(2019, 1)
        self.assertEqual(first, second)

    def test_not_equal(self):
        first = ReportMonth(2019, 1)
        second = ReportMonth(2019, 1, 15)
        self.assertEqual(hash(first), hash(second))
        self.assertNotEqual(first, second)

    def test_next_month(self):
        self.assertEqual(next_month(2018, 12), (2019, 1))
        self.assertEqual(next_month(2019, 1), (2019, 2))

    def test_months(self):
        months = list(get_months(date(2018, 10, 1), date(2019, 2, 15)))
        self.assertEqual(months, [(2018, 10), (2018, 11), (2018, 12), (2019, 1), (2019, 2)])

    def test_report_months(self):
        today = date.today()
        year = today.year
        month = today.month
        first, *_, last = report_months(date(2019, 6, 1), today)

        self.assertEqual(first, ReportMonth(2019, 6))
        self.assertEqual(last.year, year)
        self.assertEqual(last.month, month)
        self.assertEqual(last.dates, (date(year, month, 1), today))

    def test_report_diff(self):
        with self.assertRaises(AssertionError):
            report_diff(ReportMonth(2019, 1), ReportMonth(2019, 2))

        self.assertIsNone(report_diff(ReportMonth(2019, 1), ReportMonth(2019, 1)))

        start, end = report_diff(ReportMonth(2019, 1), ReportMonth(2019, 1, 15))
        self.assertEqual(start, date(2019, 1, 15))
        self.assertEqual(end, date(2019, 2, 1))
