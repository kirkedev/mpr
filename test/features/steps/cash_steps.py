from behave import when
from behave import then
from behave.api.async_step import async_run_until_complete

from mpr.cash_index import get_cash_prices
from . import format_decimal
from . import format_number
from . import server


@when('I request the CME lean hog index')
@async_run_until_complete
async def request_cash_prices(context):
    async with server():
        context.report = await get_cash_prices(context.start, context.end)


@then('I will receive a report of cash index prices from June 2019')
def verify_cash_values(context):
    print(context)
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
