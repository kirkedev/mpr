from itertools import chain
from operator import itemgetter
from typing import Iterator
from typing import Tuple

from numpy import nansum
from pandas import DataFrame
from pandas import Series
from pandas import pivot_table

from .model import Sales
from .model import to_array
from .. import create_table
from .. import with_change

bacon_cuts = ('Derind Belly 7-9#', 'Derind Belly 9-13#', 'Derind Belly 13-17#', 'Derind Belly 17-19#')

report_columns = {
    'lm_pk610': 'Negotiated',
    'lm_pk620': 'Formula'
}


def fresh_bacon(sales: Sales) -> bool:
    return sales.description in bacon_cuts


def format_column(column: Tuple[str, str]) -> str:
    value, report = column
    return f"{report_columns[report]} {value.capitalize()}"


def format_columns(table: DataFrame) -> DataFrame:
    table.columns = map(format_column, table.columns)
    return table


def format_table(weight: Series, value: Series) -> DataFrame:
    values = pivot_table(create_table(weight, value), index=['date', 'report'], aggfunc=nansum)
    price = (values.value / values.weight).rename('price')
    table = create_table(values.weight, price).unstack()

    return table[sorted(table.columns, key=itemgetter(1, 0))]


def bacon_index_report(negotiated: Iterator[Sales], formula: Iterator[Sales]) -> DataFrame:
    records = to_array(filter(fresh_bacon, chain(negotiated, formula)))
    columns = ['date', 'report', 'avg_price', 'weight']

    bacon = DataFrame.from_records(records, columns=columns).set_index(['date', 'report'])
    weight = bacon.weight.rename('weight')
    value = (bacon.avg_price * bacon.weight).rename('value')

    totals = pivot_table(create_table(weight, value), index='date', aggfunc=nansum)
    index, change = with_change(totals.value / totals.weight)

    return create_table(
        index.rename('Bacon Index'),
        change.rename('Index Change'),
        totals.weight.rename('Total Weight'),
        format_columns(format_table(weight, value)))
