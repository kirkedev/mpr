from tables import Group

from mpr import db
from ..purchase.entity import PurchaseEntity
from ..reports import PurchaseReport
from ..reports import PurchaseSection


def create() -> Group:
    group = db.connection.create_group(
        where=db.mpr,
        name=PurchaseReport.LM_HG202.name,
        title=PurchaseReport.LM_HG202.value)

    barrows_gilts_table = db.connection.create_table(
        where=group,
        name=PurchaseSection.BARROWS_AND_GILTS.name,
        description=PurchaseEntity.schema,
        title=PurchaseSection.BARROWS_AND_GILTS.value)

    barrows_gilts_table.cols.date.create_csindex()
    barrows_gilts_table.cols.report_date.create_csindex()
    barrows_gilts_table.cols.arrangement.create_index()

    return group


barrows_gilts = PurchaseEntity(PurchaseReport.LM_HG202, PurchaseSection.BARROWS_AND_GILTS)
