from datetime import date
from aiohttp.test_utils import TestServer
from aiohttp.web import Application
from behave import given

from test.routes import routes


def format_decimal(number: float) -> str:
    return '{0:.{1}f}'.format(number, 2)


def format_number(number: int) -> str:
    return '{0:.{1}f}'.format(number, 0)


def server() -> TestServer:
    app = Application()
    app.add_routes(routes)
    return TestServer(app, port=8080)


@given('a date range from June 1st to June 30th, 2019')
def set_date_range(context):
    context.start = date(2019, 6, 1)
    context.end = date(2019, 6, 30)
