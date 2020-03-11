from argparse import ArgumentParser
from asyncio import run

from datetime import date
from datetime import timedelta
from functools import singledispatch
from pandas import DataFrame

from .slaughter import get_slaughter
from .slaughter.cash_index import cash_index_report


@singledispatch
async def get(start: date, end=date.today()) -> DataFrame:
    slaughter = await get_slaughter(start - timedelta(days=5), end)
    return cash_index_report(slaughter)[start:]


@get.register(int)
async def get_recent_cash_prices(n: int) -> DataFrame:
    today = date.today()
    cash_prices = await get(today - timedelta(n + 10), today)
    return cash_prices.tail(n)


def main():  # pragma: no cover
    parser = ArgumentParser(description='Calculate the CME Lean Hog Index', usage='cash [--days=10]')
    parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)
    days = parser.parse_args().days
    print(run(get(days)))


if __name__ == '__main__':
    main()
