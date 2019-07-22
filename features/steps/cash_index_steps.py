import asyncio
from datetime import date
from numpy import isclose

from behave import given, when, then
from mpr.cash_index import get_cash_prices


@given('a date range from June 1st to June 30th, 2019')
def set_date_range(context):
    context.start = date(2019, 6, 1)
    context.end = date(2019, 6, 30)


@when('I request the CME lean hog index')
def request_cash_prices(context):
    context.report = asyncio.run(get_cash_prices(context.start, context.end))


@then('I will receive a report of cash index prices from June 2019')
def verify_report_values(context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['date']
        assert isclose(row[0], float(expected['CME Index']))
        assert isclose(row[1], float(expected['Index Change']))
        assert isclose(row[2], float(expected['Daily Avg Price']))
        assert isclose(row[3], float(expected['Price Change']))

        assert row[4] == int(expected['Negotiated Head Count'])
        assert isclose(row[5], float(expected['Negotiated Carcass Weight']))
        assert isclose(row[6], float(expected['Negotiated Net Price']))

        assert row[7] == int(expected['Market Formula Head Count'])
        assert isclose(row[8], float(expected['Market Formula Carcass Weight']))
        assert isclose(row[9], float(expected['Market Formula Net Price']))
