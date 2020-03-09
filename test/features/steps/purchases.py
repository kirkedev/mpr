from behave import then
from behave import when
from behave.api.async_step import async_run_until_complete

from mpr import purchases
from test.features.steps import format_decimal
from test.features.steps import format_number


@when("I request the purchases report")
@async_run_until_complete
async def request_purchases(context):
    context.report = await purchases.get(context. start, context.end)


@then("I will receive a report of lean hog purchase prices from June 2019")
def verify_purchases(context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['Date']
        assert format_decimal(row[0]) == expected['Purchase Index']
        assert format_decimal(row[1]) == expected['Index Change']
        assert format_decimal(row[2]) == expected['Daily Avg Price']
        assert format_decimal(row[3]) == expected['Price Change']
        assert format_number(row[4]) == expected['Negotiated Head Count']
        assert format_decimal(row[5]) == expected['Negotiated Price']
        assert format_decimal(row[6]) == expected['Negotiated Low']
        assert format_decimal(row[7]) == expected['Negotiated High']
        assert format_number(row[8]) == expected['Market Formula Head Count']
        assert format_decimal(row[9]) == expected['Market Formula Price']
        assert format_decimal(row[10]) == expected['Market Formula Low']
        assert format_decimal(row[11]) == expected['Market Formula High']
