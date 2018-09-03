from typing import Dict, Iterator, NamedTuple, Generic, TypeVar
from pathlib import Path

import tables

filepath = Path(__file__).parent / 'db.h5'

if not filepath.is_file():
  connection = tables.open_file(str(filepath), 'w', driver='H5FD_CORE')
  connection.create_group('/', 'mpr', 'USDA Mandatory Price Reporting')
else:
  connection = tables.open_file(str(filepath), 'a', driver='H5FD_CORE')
