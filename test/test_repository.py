from datetime import date
from pathlib import Path

from isoweek import Week
from pytest import fixture
from pytest import mark

from mpr.report import CutoutReport
from mpr.repository import Repository


@fixture
def repository(tmp_path: Path):
    repository = Repository(tmp_path, CutoutReport.LM_PK602)

    repository.save(Week.withdate(date(2019, 8, 20)), {
        CutoutReport.Section.CUTOUT: [{
            'report_date': '08/20/2018',
            'pork_carcass': '67.18',
            'pork_loin': '75.51',
            'pork_butt': '89.55',
            'pork_picnic': '41.82',
            'pork_rib': '113.95',
            'pork_ham': '57.52',
            'pork_belly': '77.77'
        }],
        CutoutReport.Section.VOLUME: [{
            'report_date': '08/20/2018',
            'temp_cuts_total_load': '334.74',
            'temp_process_total_load': '39.61'
        }]
    })

    return repository


@mark.asyncio
async def test_get_full_report(repository: Repository):
    archive = await repository.get(Week.withdate(date(2019, 8, 20)))
    cutout = archive.get()
    assert len(cutout[CutoutReport.Section.CUTOUT]) == 1
    assert len(cutout[CutoutReport.Section.VOLUME]) == 1


@mark.asyncio
async def test_get_report_section(repository: Repository):
    cutout = await repository.get(Week.withdate(date(2019, 8, 20)))
    assert len(cutout.get(CutoutReport.Section.CUTOUT)) == 1
