from typing import Optional
from tables import Node
from tables import Group

from mpr.data import db
from .entity.cutout import CutoutEntity


def create() -> Group:
    group = db.connection.create_group(
        where='/mpr',
        name='lm_pk602',
        title='National Daily Pork - Negotiated Sales - Morning')

    cutout_table = db.connection.create_table(
        where=group,
        name='cutout',
        description=CutoutEntity.schema,
        title='Cutout')

    cutout_table.cols.date.create_csindex()

    return group


def get(table: Optional[str] = None) -> Node:
    group = db.connection.get_node('/mpr', 'lm_pk602') if '/mpr/lm_pk602' in db.connection else create()
    return group if table is None else group[table]


class cutout(CutoutEntity):
    table = get('cutout')
