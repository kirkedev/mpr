def format_decimal(number: float) -> str:
    return '{0:.{1}f}'.format(number, 2)


def format_number(number: int) -> str:
    return '{0:.{1}f}'.format(number, 0)
