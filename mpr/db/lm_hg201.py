from tables import Group

from mpr import db
from ..slaughter.entity import SlaughterEntity
from ..reports import SlaughterReport
from ..reports import SlaughterSection


def create() -> Group:
    group = db.connection.create_group(
        where=db.mpr,
        name=SlaughterReport.LM_HG201.name,
        title=SlaughterReport.LM_HG201.value)

    barrows_gilts_table = db.connection.create_table(
        where=group,
        name=SlaughterSection.BARROWS_AND_GILTS.name,
        description=SlaughterEntity.schema,
        title=SlaughterSection.BARROWS_AND_GILTS.value)

    barrows_gilts_table.cols.date.create_csindex()
    barrows_gilts_table.cols.report_date.create_csindex()
    barrows_gilts_table.cols.arrangement.create_index()

    return group


barrows_gilts = SlaughterEntity(SlaughterReport.LM_HG201, SlaughterSection.BARROWS_AND_GILTS)
