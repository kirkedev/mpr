from os import environ
from importlib import import_module
from pathlib import Path
from typing import Optional

import tables
from tables import Node

path = Path(environ.get('DB', 'mpr/data/db/db.h5'))

if path.is_file():
    connection = tables.open_file(str(path), 'a', driver='H5FD_CORE')
else:
    connection = tables.open_file(str(path), 'w', driver='H5FD_CORE')
    connection.create_group('/', 'mpr', 'USDA Mandatory Price Reporting')


def get(group: str, table: Optional[str] = None) -> Node:
    module = import_module(f".{group}", package='mpr.data.db')
    return module.get(table)
