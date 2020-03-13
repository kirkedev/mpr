from behave import then
from behave import when
from behave.api.async_step import async_run_until_complete
from behave.runner import Context

from mpr import bacon_index
from test.features.steps import format_decimal
from test.features.steps import format_number
from test.server import server


@when('I request the CME fresh bacon index')
@async_run_until_complete
async def request_bacon_index(context: Context):
    async with server():
        context.report = await bacon_index.get(context.start, context.end)


@then('I will receive a report of fresh bacon prices from June 2019')
def verify_report_values(context: Context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['Date']
        assert format_decimal(row[0]) == expected['Bacon Index']
        assert format_decimal(row[1]) == expected['Index Change']
        assert format_number(row[2]) == expected['Total Weight']
        assert format_decimal(row[3]) == expected['Negotiated Price']
        assert format_number(row[4]) == expected['Negotiated Weight']
        assert format_decimal(row[5]) == expected['Formula Price']
        assert format_number(row[6]) == expected['Formula Weight']
