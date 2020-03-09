from behave import then
from behave import when

from mpr import purchases


@when("I request the purchases report")
def request_purchases(context):
    context.report = purchases.get(context. start, context.end)


@then("I will receive a report of prior day lean hog purchases from June 2019")
def verify_purchases(context):
    pass
