from typing import Tuple
from typing import Iterator
from pandas import DataFrame, Series

import asyncio
import pandas as pd

from mpr.data.model.slaughter import to_array
from mpr.data.model.slaughter import Slaughter
from mpr.data.model.purchase_type import Arrangement

from mpr.data.api.slaughter import fetch_slaughter

pd.options.display.float_format = '{:,.2f}'.format


def filter_types(records: Iterator[Slaughter]) -> Iterator[Slaughter]:
    return filter(lambda it: it.arrangement in (
        Arrangement.NEGOTIATED,
        Arrangement.MARKET_FORMULA,
        Arrangement.NEGOTIATED_FORMULA
    ), records)


def create_table(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    table = pd.concat([head_count, carcass_weight, net_price], axis=1).unstack()
    columns = filter(lambda it: it[1] != Arrangement.NEGOTIATED_FORMULA, table.columns)
    return table[columns]


def pivot_table(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    weight = (head_count * carcass_weight).rename('weight')
    value = (weight * net_price).rename('value')
    return pd.pivot_table(pd.concat([weight, value], axis=1), index='date')


def avg_price(value: Series, weight: Series) -> Tuple[Series, Series]:
    price = value / weight
    change = price - price.shift(1)
    return price, change


def column_title(column: Tuple[str, int]) -> str:
    (col, arrangement_id) = column
    arrangement = Arrangement(arrangement_id).name.replace('_', ' ').title()
    title = col.replace('_', ' ').title()
    return f"{arrangement} {title}"


def cash_index(records: Iterator[Slaughter]) -> DataFrame:
    columns = ['date', 'arrangement', 'head_count', 'carcass_weight', 'net_price']

    data = DataFrame(to_array(records), columns=columns).set_index(['date', 'arrangement'])
    head_count = data.head_count
    carcass_weight = data.carcass_weight
    net_price = data.net_price

    table = create_table(head_count, carcass_weight, net_price)
    table.columns = map(column_title, table.columns)

    totals = pivot_table(head_count, carcass_weight, net_price)
    daily_price, daily_change = avg_price(totals.value, totals.weight)

    rolling_totals = totals.rolling(2).sum().dropna()
    cme_index, index_change = avg_price(rolling_totals.value, rolling_totals.weight)

    return pd.concat([
        table,
        daily_price.rename('Daily Avg Price'),
        daily_change.rename('Price Change'),
        cme_index.rename('CME Index'),
        index_change.rename('Index Change')
    ], axis=1)


async def get_cash_prices(n: int) -> DataFrame:
    slaughter = await fetch_slaughter(n + 3)
    return cash_index(filter_types(slaughter)).tail(n)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Calculate the CME Lean Hog Index')
    parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)

    days = parser.parse_args().days
    print(asyncio.run(get_cash_prices(days)))
