import asyncio
from behave import when, then
from mpr.cutout_index import get_cutout_index


@when('I request the CME cutout index')
def request_cash_prices(context):
    context.report = asyncio.run(get_cutout_index(context.start, context.end))


@then('I will receive a report of cutout prices from June 2019')
def verify_report_values(context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['date']
        assert '{0:.{1}f}'.format(row[0], 2) == expected['Cutout Index']
        assert '{0:.{1}f}'.format(row[1], 2) == expected['Index Change']
        assert '{0:.{1}f}'.format(row[2], 2) == expected['Carcass Price']
        assert '{0:.{1}f}'.format(row[3], 2) == expected['Price Change']
        assert '{0:.{1}f}'.format(row[4], 2) == expected['Total Loads']
        assert '{0:.{1}f}'.format(row[5], 2) == expected['Loin Price']
        assert '{0:.{1}f}'.format(row[6], 2) == expected['Belly Price']
        assert '{0:.{1}f}'.format(row[7], 2) == expected['Butt Price']
        assert '{0:.{1}f}'.format(row[8], 2) == expected['Ham Price']
        assert '{0:.{1}f}'.format(row[9], 2) == expected['Rib Price']
        assert '{0:.{1}f}'.format(row[10], 2) == expected['Picnic Price']
