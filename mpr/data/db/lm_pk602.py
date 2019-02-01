from typing import Optional
from tables import Node, Group

import db
from model.cutout import Cutout

def create() -> Group:
  group = db.connection.create_group('/mpr', name='lm_pk602',
    title='National Daily Pork - Negotiated Sales - Morning')

  cutout_table = db.connection.create_table(group, 'cutout', Cutout.schema,
    'Volume and pricing for primal pork cuts as of 11:00am central time')

  cutout_table.cols.date.create_csindex()

  return group

def get(table: Optional[str] = None) -> Node:
  group = db.connection.get_node('/mpr', 'lm_pk602') if '/mpr/lm_pk602' in db.connection else create()
  return group if table is None else group[table]

class cutout(Cutout):
  table = get('cutout')
