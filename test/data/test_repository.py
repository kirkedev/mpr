from datetime import date
from pathlib import Path

from isoweek import Week
from pytest import fixture
from pytest import mark

from mpr.report import CutoutReport
from mpr.data.archive import Archive
from mpr.data.repository import Repository


@fixture
async def repository(tmp_path: Path):
    repository = Repository(CutoutReport.LM_PK602, tmp_path)

    Archive(Path(repository), Week.withdate(date(2019, 8, 20))).save({
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
async def test_get_report_from_api(repository: Repository, mpr_server):
    async with mpr_server:
        archive = await repository.get(Week.withdate(date(2019, 6, 6)))

    report = archive.get()
    assert len(report) == 14

    cutout = report[CutoutReport.Section.CUTOUT]
    assert len(cutout) == 5
    assert cutout[0]['report_date'] == '06/03/2019'
    assert cutout[1]['report_date'] == '06/04/2019'
    assert cutout[-1]['report_date'] == '06/07/2019'

    volume = report[CutoutReport.Section.VOLUME]
    assert len(volume) == 5
    assert volume[0]['report_date'] == '06/03/2019'
    assert volume[1]['report_date'] == '06/04/2019'
    assert volume[-1]['report_date'] == '06/07/2019'


@mark.asyncio
async def test_query_sections(repository: Repository, mpr_server):
    async with mpr_server:
        cutout, volume = await repository.query(date(2019, 6, 1), date(2019, 6, 10),
            CutoutReport.Section.CUTOUT, CutoutReport.Section.VOLUME)

    assert len(cutout) == 6
    assert len(volume) == 6
