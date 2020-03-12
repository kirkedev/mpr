from argparse import ArgumentParser
from asyncio import run
from datetime import date
from datetime import timedelta
from functools import singledispatch

from pandas import DataFrame

from mpr import cutout
from .cutout.cutout_index import cutout_report


@singledispatch
async def get(start: date, end=date.today()) -> DataFrame:
    records = await cutout.afternoon(start - timedelta(10), end)
    return cutout_report(records)[start:]


@get.register(int)
async def get_recent(n: int) -> DataFrame:
    today = date.today()
    cutout_index = await get(today - timedelta(days=n + 10), today)
    return cutout_index.tail(n)


def main():  # pragma: no cover
    parser = ArgumentParser(description='Calculate the CME Cutout Index', usage='cash [--days=10]')
    parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)
    days = parser.parse_args().days
    print(run(get(days)))


if __name__ == '__main__':
    main()
