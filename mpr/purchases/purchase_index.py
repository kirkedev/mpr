from operator import itemgetter
from typing import Iterator
from typing import Tuple

import pandas as pd
from pandas import DataFrame
from pandas import Series

from .model import Purchase
from .model import to_array
from .. import create_table
from .. import with_change
from ..purchase_type import Arrangement
from ..purchase_type import Basis

total_value = lambda head_count, price: head_count * price
weighted_price = lambda value, head_count: value / head_count


def filter_arrangement(records: Iterator[Purchase]) -> Iterator[Purchase]:
    return filter(lambda it: it.basis == Basis.CARCASS and it.arrangement in (
        Arrangement.NEGOTIATED,
        Arrangement.MARKET_FORMULA
    ), records)


def format_table(head_count: Series, avg_price: Series, low_price: Series, high_price: Series) -> DataFrame:
    table = create_table(head_count, avg_price, low_price, high_price).unstack()
    columns = sorted(table.columns, key=itemgetter(1))
    return table[columns]


def format_columns(table: DataFrame) -> DataFrame:
    table.columns = map(format_column, table.columns)
    return table


def format_column(column: Tuple[str, int]) -> str:
    (field, arrangement) = column
    return f"{Arrangement(arrangement).name} {field}".replace('_', ' ').title()


def purchase_report(purchases: Iterator[Purchase]) -> DataFrame:
    records = to_array(filter_arrangement(purchases))
    columns = ['date', 'arrangement', 'head_count', 'avg_price', 'low_price', 'high_price']
    data = DataFrame.from_records(records, columns=columns).set_index(['date', 'arrangement'])

    head_count = data.head_count
    avg_price = data.avg_price.rename('Price')
    low_price = data.low_price.rename('Low')
    high_price = data.high_price.rename('High')
    value = total_value(head_count=head_count, price=avg_price).rename('value')

    total_values = pd.pivot_table(create_table(value, head_count), index='date')
    daily_price, daily_change = with_change(weighted_price(**total_values))

    rolling_totals = total_values.rolling(5).sum().dropna()
    index, index_change = with_change(weighted_price(**rolling_totals))

    return create_table(
        index.rename('Purchase Index'),
        index_change.rename('Index Change'),
        daily_price.rename('Daily Avg Price'),
        daily_change.rename('Price Change'),
        format_columns(format_table(head_count, avg_price, low_price, high_price)))
