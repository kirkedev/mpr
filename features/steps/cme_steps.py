import asyncio
from behave import when, then

from mpr.cash_index import get_cash_prices
from mpr.cutout_index import get_cutout_index
from features.steps.lib import format_decimal, format_number


@when('I request the CME lean hog index')
def request_cash_prices(context):
    context.report = asyncio.run(get_cash_prices(context.start, context.end))


@then('I will receive a report of cash index prices from June 2019')
def verify_cash_values(context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['date']
        assert format_decimal(row[0]) == expected['CME Index']
        assert format_decimal(row[1]) == expected['Index Change']
        assert format_decimal(row[2]) == expected['Daily Avg Price']
        assert format_decimal(row[3]) == expected['Price Change']
        assert format_number(row[4]) == expected['Negotiated Head Count']
        assert format_decimal(row[5]) == expected['Negotiated Carcass Weight']
        assert format_decimal(row[6]) == expected['Negotiated Net Price']
        assert format_number(row[7]) == expected['Market Formula Head Count']
        assert format_decimal(row[8]) == expected['Market Formula Carcass Weight']
        assert format_decimal(row[9]) == expected['Market Formula Net Price']


@when('I request the CME cutout index')
def request_cutout(context):
    context.report = asyncio.run(get_cutout_index(context.start, context.end))


@then('I will receive a report of cutout prices from June 2019')
def verify_cutout_values(context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['date']
        assert format_decimal(row[0]) == expected['Cutout Index']
        assert format_decimal(row[1]) == expected['Index Change']
        assert format_decimal(row[2]) == expected['Carcass Price']
        assert format_decimal(row[3]) == expected['Price Change']
        assert format_decimal(row[4]) == expected['Total Loads']
        assert format_decimal(row[5]) == expected['Loin Price']
        assert format_decimal(row[6]) == expected['Belly Price']
        assert format_decimal(row[7]) == expected['Butt Price']
        assert format_decimal(row[8]) == expected['Ham Price']
        assert format_decimal(row[9]) == expected['Rib Price']
        assert format_decimal(row[10]) == expected['Picnic Price']
