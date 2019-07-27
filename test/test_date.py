from datetime import date
from unittest import TestCase

from mpr.date import quarter, get_quarter


class TestDate(TestCase):
    def test_first_quarter(self):
        start, end = quarter(2019, 0)
        self.assertEqual(start, date(2019, 1, 1))
        self.assertEqual(end, date(2019, 4, 1))
        self.assertEqual(get_quarter(date(2019, 2, 15)), 0)

    def test_second_quarter(self):
        start, end = quarter(2019, 1)
        self.assertEqual(start, date(2019, 4, 1))
        self.assertEqual(end, date(2019, 7, 1))
        self.assertEqual(get_quarter(date(2019, 5, 15)), 1)

    def test_third_quarter(self):
        start, end = quarter(2019, 2)
        self.assertEqual(start, date(2019, 7, 1))
        self.assertEqual(end, date(2019, 10, 1))
        self.assertEqual(get_quarter(date(2019, 8, 15)), 2)

    def test_fourth_quarter(self):
        start, end = quarter(2019, 3)
        self.assertEqual(start, date(2019, 10, 1))
        self.assertEqual(end, date(2020, 1, 1))
        self.assertEqual(get_quarter(date(2019, 11, 15)), 3)
