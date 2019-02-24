from typing import Tuple
from typing import Iterator
from datetime import date
from operator import itemgetter
from functools import singledispatch

import pandas as pd
from pandas import Series
from pandas import DataFrame

from mpr.data.api.slaughter import fetch_slaughter
from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.slaughter import Slaughter
from mpr.data.model.slaughter import to_array

from . import total_weight
from . import total_value
from . import weighted_price
from . import filter_types

pd.options.display.float_format = '{:,.2f}'.format


def create_table(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    table = pd.concat([head_count, carcass_weight, net_price], axis=1).unstack()

    get_arrangement = itemgetter(1)
    columns = filter(lambda it: get_arrangement(it) != Arrangement.NEGOTIATED_FORMULA, table.columns)
    columns = sorted(columns, key=get_arrangement)

    return table[columns]


def column_title(column: Tuple[str, int]) -> str:
    (field, arrangement) = column
    field = field.replace('_', ' ').title()
    arrangement = Arrangement(arrangement).name.replace('_', ' ').title()

    return f"{arrangement} {field}"


def weights_and_values(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    weight = total_weight(head_count=head_count, weight=carcass_weight).rename('weight')
    value = total_value(weight=weight, price=net_price).rename('value')

    return pd.pivot_table(pd.concat([weight, value], axis=1), index='date')


def with_change(values: Series) -> Tuple[Series, Series]:
    values = values.round(decimals=2)
    change = values - values.shift(1)

    return values, change


def cash_prices_report(records: Iterator[Slaughter]) -> DataFrame:
    array = to_array(filter_types(records))
    columns = ['date', 'arrangement', 'head_count', 'carcass_weight', 'net_price']
    data = DataFrame(array, columns=columns).set_index(['date', 'arrangement'])

    head_count = data.head_count
    carcass_weight = data.carcass_weight
    net_price = data.net_price

    table = create_table(head_count, carcass_weight, net_price)
    table.columns = map(column_title, table.columns)

    totals = weights_and_values(head_count, carcass_weight, net_price)
    daily_price, daily_change = with_change(weighted_price(value=totals.value, weight=totals.weight))

    rolling_totals = totals.rolling(2).sum().dropna()
    cme_index, index_change = with_change(weighted_price(value=rolling_totals.value, weight=rolling_totals.weight))

    return pd.concat([
        table,
        daily_price.rename('Daily Avg Price'),
        daily_change.rename('Price Change'),
        cme_index.rename('CME Index'),
        index_change.rename('Index Change')
    ], axis=1)


@singledispatch
async def get_cash_prices(start: date, end=date.today()) -> DataFrame:
    slaughter = await fetch_slaughter(start, end)
    return cash_prices_report(slaughter)


@get_cash_prices.register(int)
async def get_cash_prices_days(n: int) -> DataFrame:
    slaughter = await fetch_slaughter(n + 3)
    return cash_prices_report(slaughter).tail(n)
