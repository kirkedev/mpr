from unittest import TestCase
from . import load_resource

attributes = list(load_resource('cash_prices.xml'))
print(attributes)


class CashIndexTest(TestCase):
    def test_total_value(self):
        pass
