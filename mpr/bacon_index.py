from argparse import ArgumentParser
from asyncio import run
from datetime import date
from datetime import timedelta
from functools import singledispatch

from isoweek import Week
from pandas import DataFrame

from mpr.sales import Cut
from mpr.sales import weekly_formula
from mpr.sales import weekly_negotiated
from mpr.sales.bacon_index import bacon_index_report


@singledispatch
async def get(start: date, end: date) -> DataFrame:
    formula_sales = await weekly_formula(start, end, Cut.BELLY)
    negotiated_sales = await weekly_negotiated(start, end, Cut.BELLY)
    return bacon_index_report(formula_sales, negotiated_sales)[start:end]


@get.register(int)
async def get_recent(n: int) -> DataFrame:
    today = date.today()
    start = Week.withdate(today - timedelta(weeks=n))
    end = Week.withdate(today)

    report = await get(start, end)
    return report.tail(n)


def main():  # pragma: no cover
    parser = ArgumentParser(description='Calculate the CME Fresh Bacon Index', usage='bacon [--weeks=10]')
    parser.add_argument('--weeks', help='How many weeks to show', dest='weeks', type=int, default=8)
    n = parser.parse_args().weeks
    print(run(get(n)))


if __name__ == '__main__':
    main()
