from behave import then
from behave import when
from behave.api.async_step import async_run_until_complete

from mpr import purchases


@when("I request the purchases report")
@async_run_until_complete
async def request_purchases(context):
    context.report = await purchases.get(context. start, context.end)


@then("I will receive a report of prior day lean hog purchases from June 2019")
def verify_purchases(context):
    pass
