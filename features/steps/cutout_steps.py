import asyncio
from behave import when, then
from mpr import cutout


@when("I request the daily pork cutout morning report")
def request_lm_hg202(context):
    context.report = asyncio.run(cutout.morning(context.start, context.end))


@then("I will receive a list of negotiated pork sales records as of 11:00am central time")
def verify_lm_hg202_values(context):
    pass


@when("I request the daily pork cutout afternoon report")
def request_lm_hg203(context):
    context.report = asyncio.run(cutout.afternoon(context.start, context.end))


@then("I will receive a list of negotiated pork sales records as of 3:00pm central time")
def verify_lm_hg203_values(context):
    pass
