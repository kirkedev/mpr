from typing import Tuple
from typing import Iterator

import asyncio
import pandas as pd
from pandas import DataFrame, Series

from data.api.slaughter import get_slaughter, Record as SlaughterRecord


def filter_types(record: SlaughterRecord) -> bool:
    return record.purchase_type in (
        'Prod. Sold Negotiated',
        'Prod. Sold Negotiated Formula',
        'Prod. Sold Swine or Pork Market Formula')


compute_weight = lambda head_count, carcass_weight: head_count * carcass_weight
compute_value = lambda total_weight, net_price: total_weight * net_price
compute_price = lambda total_value, total_weight: total_value / total_weight


def compute_change(series: Series) -> Series:
    return series - series.shift(1)


def compute_cash_index(records: Iterator[SlaughterRecord]) -> DataFrame:
    slaughter = DataFrame.from_records(records, columns=SlaughterRecord._fields)

    slaughter['purchase_type'] = slaughter['purchase_type'].replace({
        'Prod. Sold Negotiated': 'Negotiated',
        'Prod. Sold Swine or Pork Market Formula': 'Market Formula',
        'Prod. Sold Negotiated Formula': 'Negotiated Formula'
    })

    slaughter = slaughter.set_index(['date', 'purchase_type'])

    total_weight = compute_weight(slaughter['head_count'], slaughter['carcass_weight']).rename('total_weight')
    total_value = compute_value(total_weight, slaughter['net_price']).rename('total_value')

    totals = pd.pivot_table(pd.concat([total_weight, total_value], axis=1), index='date')
    daily_price = compute_price(totals['total_value'], totals['total_weight']).rename('Daily Weighted Price')
    price_change = compute_change(daily_price).rename('Price Change')

    rolling_totals = totals.rolling(2).sum().dropna()
    cme_index = compute_price(rolling_totals['total_value'], rolling_totals['total_weight']).rename('CME Index')
    index_change = compute_change(cme_index).rename('Index Change')

    table = pd.concat([slaughter['head_count'], slaughter['carcass_weight'], slaughter['net_price']], axis=1).unstack()
    cols = filter(lambda it: it[1] != 'Negotiated Formula', table.columns)
    cols = sorted(cols, key=lambda it: ('Negotiated', 'Market Formula').index(it[1]))

    table = table[cols]

    def rename_cols(it: Tuple[str, str]) -> str:
        (col, purchase_type) = it
        return purchase_type + ' ' + col.replace('_', ' ').title()

    table.columns = map(rename_cols, table.columns)

    return pd.concat([table, daily_price, price_change, cme_index, index_change], axis=1)


def get_cash_prices(days: int) -> DataFrame:
    slaughter = asyncio.run(get_slaughter(days + 3))
    return compute_cash_index(filter(filter_types, slaughter)).tail(days)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Calculate the CME Lean Hog Index')
    parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)

    days = parser.parse_args().days
    print(get_cash_prices(days=days))
