import asyncio
from datetime import datetime
from itertools import zip_longest
from operator import itemgetter

from behave import when, then
from mpr import purchase
from mpr.purchase import Purchase
from mpr.purchase.api import parse_attributes

sort_key = itemgetter(1, 2, 3, 4)


def from_table_row(row) -> Purchase:
    return parse_attributes({
        'report_date': datetime.strptime(row['Report Date'], "%Y-%m-%d").strftime("%m/%d/%Y"),
        'reported_for_date': datetime.strptime(row['Reported For Date'], "%Y-%m-%d").strftime("%m/%d/%Y"),
        'purchase_type': row['Purchase Type'],
        'head_count': row['Head Count'],
        'wtd_avg': row['Weighted Average Price'],
        'price_low': row['Price Range Low'],
        'price_high': row['Price Range High']
    })


@when("I request the daily direct hog prior day report")
def request_lm_hg200(context):
    context.report = asyncio.run(purchase.prior_day(context.start, context.end))


@then("I will receive a list of daily hog purchase records for the prior day")
def verify_lm_hg200_values(context):
    rows = zip_longest(sorted(map(from_table_row, context.table), key=sort_key), sorted(context.report, key=sort_key))
    assert all(expected == actual for expected, actual in rows)


@when("I request the daily direct hog morning report")
def request_lm_hg202(context):
    context.report = asyncio.run(purchase.morning(context.start, context.end))


@then("I will receive a list of daily hog purchase records as of 11:00am central time")
def verify_lm_hg202_values(context):
    rows = zip_longest(sorted(map(from_table_row, context.table), key=sort_key), sorted(context.report, key=sort_key))
    assert all(expected == actual for expected, actual in rows)


@when("I request the daily direct hog afternoon report")
def request_lm_hg203(context):
    context.report = asyncio.run(purchase.afternoon(context.start, context.end))


@then("I will receive a list of daily hog purchase records as of 3:00pm central time")
def verify_lm_hg203_values(context):
    rows = zip_longest(sorted(map(from_table_row, context.table), key=sort_key), sorted(context.report, key=sort_key))
    assert all(expected == actual for expected, actual in rows)
