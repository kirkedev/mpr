from typing import Optional
from tables import File
from tables import Node
from tables import Group

from mpr.data import db
from mpr.data.db.model.purchase import Purchase


def create(connection: File = db.connection) -> Group:
    group = connection.create_group(
        where='/mpr',
        name='lm_hg200',
        title='Daily Direct Hog Prior Day - Purchased Swine')

    barrows_gilts_table = connection.create_table(
        where=group,
        name='barrows_gilts',
        description=Purchase.schema)

    barrows_gilts_table.cols.date.create_csindex()

    return group


def get(connection: File = db.connection, table: Optional[str] = None) -> Node:
    group = connection.get_node('/mpr', 'lm_hg200') if '/mpr/lm_hg200' in connection else create()
    return group if table is None else group[table]


class barrows_gilts(Purchase):
    table = get('barrows_gilts')
