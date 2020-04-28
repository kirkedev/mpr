from argparse import ArgumentParser
from asyncio import run
from datetime import date
from functools import singledispatch

from isoweek import Week
from pandas import DataFrame

from .sales import Cut
from .sales import lm_pk610
from .sales import weekly_formula
from .sales import weekly_negotiated
from .sales.bacon_index import bacon_index_report


@singledispatch
async def get(start: date, end: date) -> DataFrame:
    first = Week.withdate(start) - 1
    last = Week.withdate(end)
    monday = first.monday()

    if last.day(lm_pk610.weekday) > lm_pk610.latest:
        last -= 1

    end = last.saturday()
    formula_sales = await weekly_formula(monday, end, Cut.BELLY)
    negotiated_sales = await weekly_negotiated(monday, end, Cut.BELLY)

    return bacon_index_report(formula_sales, negotiated_sales)[start:end]


@get.register(int)
async def get_recent(n: int) -> DataFrame:
    today = date.today()
    first = Week.withdate(today) - n - 1
    report = await get(first.monday(), today)
    return report.tail(n)


def main():
    parser = ArgumentParser(description='Calculate the CME Fresh Bacon Index', usage='bacon [--weeks=8]')
    parser.add_argument('--weeks', help='How many weeks to show', dest='weeks', type=int, default=8)
    weeks = parser.parse_args().weeks
    print(run(get(weeks)))


if __name__ == '__main__':
    main()
