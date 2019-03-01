from typing import Optional
from tables import Node
from tables import Group

from mpr import db
from .entity.purchase import PurchaseEntity


def create() -> Group:
    group = db.connection.create_group(
        where='/mpr',
        name='lm_hg200',
        title='Daily Direct Hog Prior Day - Purchased Swine')

    barrows_gilts_table = db.connection.create_table(
        where=group,
        name='barrows_gilts',
        description=PurchaseEntity.schema,
        title='Barrows and Gilts')

    barrows_gilts_table.cols.date.create_csindex()
    barrows_gilts_table.cols.arrangement.create_index()

    return group


def get(table: Optional[str] = None) -> Node:
    group = db.connection.get_node('/mpr', 'lm_hg200') if '/mpr/lm_hg200' in db.connection else create()
    return group if table is None else group[table]


class barrows_gilts(PurchaseEntity):
    table = get('barrows_gilts')