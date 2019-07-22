from tables import Group

from mpr import db
from ..reports import CutoutReport
from ..reports import CutoutSection
from ..cutout.entity import CutoutEntity


def create() -> Group:
    group = db.connection.create_group(
        where=db.mpr,
        name=CutoutReport.LM_PK602.name,
        title=CutoutReport.LM_PK602.value)

    cutout_table = db.connection.create_table(
        where=group,
        name=CutoutSection.CUTOUT.name,
        description=CutoutEntity.schema,
        title=CutoutSection.CUTOUT.value)

    cutout_table.cols.date.create_csindex()
    cutout_table.cols.report_date.create_csindex()

    return group


cutout = CutoutEntity(CutoutReport.LM_PK602, CutoutSection.CUTOUT)
