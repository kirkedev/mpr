from typing import Optional
from tables import Node, Group

import db
from model.purchase import Purchase

def create() -> Group:
  group = db.connection.create_group('/mpr', name='lm_hg200',
    title='Daily Direct Hog Prior Day - Purchased Swine')

  barrows_gilts_table = db.connection.create_table(group, 'barrows_gilts', Purchase.schema,
    'Prior day volume and pricing for barrows and gilts')

  barrows_gilts_table.cols.date.create_csindex()

  return group

def get(table: Optional[str] = None) -> Node:
  group = db.connection.get_node('/mpr', 'lm_hg200') if '/mpr/lm_hg200' in db.connection else create()
  return group if table is None else group[table]

class barrows_gilts(Purchase):
  table = get('barrows_gilts')
