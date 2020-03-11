from datetime import date
from datetime import timedelta
from functools import singledispatch
from pandas import DataFrame

from mpr import purchase
from .purchase.report import purchase_report


from argparse import ArgumentParser
from asyncio import run


@singledispatch
async def get(start: date, end=date.today()) -> DataFrame:
    records = await purchase.prior_day(start - timedelta(10), end)
    return purchase_report(records)[start:]


@get.register(int)
async def get_recent(n: int) -> DataFrame:
    today = date.today()
    purchases = await get(today - timedelta(days=n + 10), today)
    return purchases.tail(n)


def main():  # pragma: no cover
    parser = ArgumentParser(description='Calculate Average Lean Hog Purchase Prices', usage='cash [--days=10]')
    parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)
    days = parser.parse_args().days
    print(run(get(days)))


if __name__ == '__main__':
    main()
