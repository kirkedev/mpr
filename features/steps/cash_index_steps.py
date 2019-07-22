import asyncio
from datetime import date
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
        assert '{0:.{1}f}'.format(row[0], 2) == expected['CME Index']
        assert '{0:.{1}f}'.format(row[1], 2) == expected['Index Change']
        assert '{0:.{1}f}'.format(row[2], 2) == expected['Daily Avg Price']
        assert '{0:.{1}f}'.format(row[3], 2) == expected['Price Change']

        assert row[4] == int(expected['Negotiated Head Count'])
        assert '{0:.{1}f}'.format(row[5], 2) == expected['Negotiated Carcass Weight']
        assert '{0:.{1}f}'.format(row[6], 2) == expected['Negotiated Net Price']

        assert row[7] == int(expected['Market Formula Head Count'])
        assert '{0:.{1}f}'.format(row[8], 2) == expected['Market Formula Carcass Weight']
        assert '{0:.{1}f}'.format(row[9], 2) == expected['Market Formula Net Price']
