import asyncio
from numpy import isclose
from behave import when, then
from mpr.cutout_index import get_cutout_index


@when('I request the CME cutout index')
def request_cash_prices(context):
    context.report = asyncio.run(get_cutout_index(context.start, context.end))


@then('I will receive a report of cutout prices from June 2019')
def verify_report_values(context):
    for expected, (index, row) in zip(context.table, context.report.iterrows()):
        assert index.strftime('%Y-%m-%d') == expected['date']
        assert isclose(round(row[0], 2), float(expected['Cutout Index']))
        assert isclose(round(row[1], 2), float(expected['Index Change']))
        assert isclose(round(row[2], 2), float(expected['Carcass Price']))
        assert isclose(round(row[3], 2), float(expected['Price Change']))
        assert isclose(round(row[4], 2), float(expected['Total Loads']))
        assert isclose(round(row[5], 2), float(expected['Loin Price']))
        assert isclose(round(row[6], 2), float(expected['Belly Price']))
        assert isclose(round(row[7], 2), float(expected['Butt Price']))
        assert isclose(round(row[8], 2), float(expected['Ham Price']))
        assert isclose(round(row[9], 2), float(expected['Rib Price']))
        assert isclose(round(row[10], 2), float(expected['Picnic Price']))
