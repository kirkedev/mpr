from os import environ
from typing import Optional
from importlib import import_module
from pathlib import Path

import tables

path = Path(environ.get('DB', 'mpr/db/db.h5'))

if path.is_file():
    connection = tables.open_file(str(path), 'a', driver='H5FD_CORE')
else:
    connection = tables.open_file(str(path), 'w', driver='H5FD_CORE')
    connection.create_group('/', 'mpr', 'USDA Mandatory Price Reporting')


def get(group: str, table: Optional[str] = None):
    group = import_module(f".{group}", package='mpr.db')
    return group if table is None else getattr(group, table)
