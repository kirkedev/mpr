from typing import Tuple
from typing import Iterator
from operator import itemgetter

import pandas as pd
from pandas import Series
from pandas import DataFrame

from mpr.data.model.purchase_type import Arrangement
from mpr.data.model.slaughter import Slaughter
from mpr.data.model.slaughter import to_array

from .. import with_change
from .. import create_table

total_weight = lambda head_count, weight: head_count * weight
total_value = lambda weight, price: weight * price
weighted_price = lambda value, weight: value / weight


def filter_types(records: Iterator[Slaughter]) -> Iterator[Slaughter]:
    return filter(lambda it: it.arrangement in (
        Arrangement.NEGOTIATED,
        Arrangement.MARKET_FORMULA,
        Arrangement.NEGOTIATED_FORMULA
    ), records)


def format_table(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    table = create_table(head_count, carcass_weight, net_price).unstack()

    get_arrangement = itemgetter(1)
    columns = filter(lambda it: get_arrangement(it) != Arrangement.NEGOTIATED_FORMULA, table.columns)
    columns = sorted(columns, key=get_arrangement)

    table = table[columns]
    table.columns = map(column_title, table.columns)

    return table


def column_title(column: Tuple[str, int]) -> str:
    (field, arrangement) = column
    field = field.replace('_', ' ').title()
    arrangement = Arrangement(arrangement).name.replace('_', ' ').title()

    return f"{arrangement} {field}"


def weights_and_values(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    weight = total_weight(head_count=head_count, weight=carcass_weight).rename('weight')
    value = total_value(weight=weight, price=net_price).rename('value')

    return pd.pivot_table(pd.concat([weight, value], axis=1), index='date')


def cash_index_report(records: Iterator[Slaughter]) -> DataFrame:
    array = to_array(filter_types(records))
    columns = ['date', 'arrangement', 'head_count', 'carcass_weight', 'net_price']
    data = DataFrame(array, columns=columns).set_index(['date', 'arrangement'])

    head_count = data.head_count
    carcass_weight = data.carcass_weight
    net_price = data.net_price

    totals = weights_and_values(head_count, carcass_weight, net_price)
    daily_price, daily_change = with_change(weighted_price(value=totals.value, weight=totals.weight))

    rolling_totals = totals.rolling(2).sum().dropna()
    cme_index, index_change = with_change(weighted_price(value=rolling_totals.value, weight=rolling_totals.weight))

    return create_table(
        cme_index.rename('CME Index'),
        index_change.rename('Index Change'),
        daily_price.rename('Daily Avg Price'),
        daily_change.rename('Price Change'),
        format_table(head_count, carcass_weight, net_price))
