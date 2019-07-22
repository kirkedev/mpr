from os import environ
from typing import Optional
from importlib import import_module
from pathlib import Path

import tables

from ..reports import Report
from ..reports import Section

path = Path(environ.get('DB', 'mpr/db/db.h5'))

if path.is_file():
    connection = tables.open_file(str(path), 'a', driver='H5FD_CORE')
else:
    connection = tables.open_file(str(path), 'w', driver='H5FD_CORE')
    connection.create_group('/', 'mpr', 'USDA Mandatory Price Reporting')

mpr = connection.get_node('/mpr')


def get(report: Report, section: Optional[Section] = None):
    if report.name not in mpr:
        group = import_module(f".{report.name}", package='mpr.db')
        group.create()

    group = mpr[report.name]

    return group[section.name] if section else group
