import argparse
import asyncio

from .report import get_cash_prices

parser = argparse.ArgumentParser(description='Calculate the CME Lean Hog Index')
parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)

days = parser.parse_args().days
print(asyncio.run(get_cash_prices(days)))
