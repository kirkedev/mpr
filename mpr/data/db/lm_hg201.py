from typing import Optional
from tables import Node
from tables import Group

from mpr.data import db
from mpr.data.db.model.slaughter import Slaughter


def create() -> Group:
    group = db.connection.create_group(
        where='/mpr',
        name='lm_hg201',
        title='Daily Direct Hog Prior Day - Slaughtered Swine')

    barrows_gilts_table = db.connection.create_table(
        where=group,
        name='barrows_gilts',
        description=Slaughter.schema,
        title='Barrows and Gilts')

    barrows_gilts_table.cols.date.create_csindex()

    return group


def get(table: Optional[str] = None) -> Node:
    group = db.connection.get_node('/mpr', 'lm_hg201') if '/mpr/lm_hg201' in db.connection else create()
    return group if table is None else group[table]


class barrows_gilts(Slaughter):
    table = get('barrows_gilts')
