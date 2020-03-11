from typing import Tuple
from typing import Iterator
from operator import itemgetter

import pandas as pd
from pandas import Series
from pandas import DataFrame

from .model import Slaughter
from .model import to_array
from .. import create_table
from .. import with_change
from ..purchase_type import Arrangement

total_weight = lambda head_count, weight: head_count * weight
total_value = lambda weight, price: weight * price
weighted_price = lambda value, weight: value / weight


def filter_arrangement(records: Iterator[Slaughter]) -> Iterator[Slaughter]:
    return filter(lambda it: it.arrangement in (
        Arrangement.NEGOTIATED,
        Arrangement.MARKET_FORMULA,
        Arrangement.NEGOTIATED_FORMULA
    ), records)


def format_table(head_count: Series, carcass_weight: Series, net_price: Series) -> DataFrame:
    table = create_table(head_count, carcass_weight, net_price).unstack()

    get_arrangement = itemgetter(1)
    columns = filter(lambda it: get_arrangement(it) != Arrangement.NEGOTIATED_FORMULA, table.columns)
    return table[sorted(columns, key=get_arrangement)]


def format_columns(table: DataFrame) -> DataFrame:
    table.columns = map(format_column, table.columns)
    return table


def format_column(column: Tuple[str, int]) -> str:
    (field, arrangement) = column
    return f"{Arrangement(arrangement).name} {field}".replace('_', ' ').title()


def cash_index_report(slaughter: Iterator[Slaughter]) -> DataFrame:
    records = to_array(filter_arrangement(slaughter))
    columns = ['date', 'arrangement', 'head_count', 'carcass_weight', 'net_price']
    data = DataFrame(records, columns=columns).set_index(['date', 'arrangement'])

    head_count = data.head_count
    carcass_weight = data.carcass_weight
    net_price = data.net_price

    weight = total_weight(head_count=head_count, weight=carcass_weight).rename('weight')
    value = total_value(weight=weight, price=net_price).rename('value')

    total_values = pd.pivot_table(create_table(weight, value), index='date')
    daily_price, daily_change = with_change(weighted_price(**total_values))

    rolling_totals = total_values.rolling(2).sum().dropna()
    cme_index, index_change = with_change(weighted_price(**rolling_totals))

    return create_table(
        cme_index.rename('CME Index'),
        index_change.rename('Index Change'),
        daily_price.rename('Daily Avg Price'),
        daily_change.rename('Price Change'),
        format_columns(format_table(head_count, carcass_weight, net_price)))
