from datetime import date
from behave import given


def format_decimal(number: float) -> str:
    return '{0:.{1}f}'.format(number, 2)


def format_number(number: int) -> str:
    return '{0:.{1}f}'.format(number, 0)


@given('a date range from June 1st to June 30th, 2019')
def set_date_range(context):
    context.start = date(2019, 6, 1)
    context.end = date(2019, 6, 30)
