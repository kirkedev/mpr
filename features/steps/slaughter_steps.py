import asyncio
from behave import when, then
from mpr import slaughter


@when("I request the daily slaughtered swine report")
def request_lm_hg201(context):
    context.report = asyncio.run(slaughter.get_slaughter(context.start, context.end))


@then("I will receive a list of slaughtered swine records for the prior day")
def verify_lm_hg201_values(context):
    pass
