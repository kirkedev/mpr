from datetime import date
from typing import Optional
from tables import Node, Group

import db
from model.slaughter import Slaughter

def create() -> Group:
  group = db.connection.create_group('/mpr', name='lm_hg201',
    title='Daily Direct Hog Prior Day - Slaughtered Swine')

  barrows_gilts_table = db.connection.create_table(group, 'barrows_gilts', Slaughter.schema,
    'Prior day volume, pricing, and weights for slaughtered barrows and gilts')

  barrows_gilts_table.cols.date.create_csindex()

  return group

def get(table: Optional[str] = None) -> Node:
  group = db.connection.get_node('/mpr', 'lm_hg201') if '/mpr/lm_hg201' in db.connection else create()
  return group if table is None else group[table]

class barrows_gilts(Slaughter):
  table = get('barrows_gilts')
