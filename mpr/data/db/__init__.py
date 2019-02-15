from pathlib import Path

import os
import tables

path = Path('test/db' if os.environ['ENV'] == 'TEST' else 'mpr/data/db') / 'db.h5'

if path.is_file():
    connection = tables.open_file(str(path), 'a', driver='H5FD_CORE')
else:
    connection = tables.open_file(str(path), 'w', driver='H5FD_CORE')
    connection.create_group('/', 'mpr', 'USDA Mandatory Price Reporting')
