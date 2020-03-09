from datetime import date
from pathlib import Path

from pytest import fixture
from pytest import mark

from mpr.report import CutoutReport
from mpr.data.repository import Repository
from mpr.report import lm_pk602
from test.server import server


@fixture
async def repository(tmp_path: Path):
    repository = Repository(lm_pk602, tmp_path)
    assert Path(repository).name == 'lm_pk602'
    return repository


@mark.asyncio
async def test_query_section(repository: Repository):
    async with server():
        cutout = await repository.query(date(2019, 5, 26), date(2019, 6, 6), CutoutReport.Section.CUTOUT)

    assert len(cutout) == 8
    assert cutout[0]['report_date'] == '05/28/2019'
    assert cutout[1]['report_date'] == '05/29/2019'
    assert cutout[-1]['report_date'] == '06/06/2019'


@mark.asyncio
async def test_query_sections(repository: Repository):
    async with server():
        cutout, volume = await repository.query(date(2019, 6, 1), date(2019, 6, 10),
            CutoutReport.Section.CUTOUT, CutoutReport.Section.VOLUME)

    assert len(cutout) == 6
    assert cutout[0]['report_date'] == '06/03/2019'
    assert cutout[1]['report_date'] == '06/04/2019'
    assert cutout[-1]['report_date'] == '06/10/2019'

    assert len(volume) == 6
    assert volume[0]['report_date'] == '06/03/2019'
    assert volume[1]['report_date'] == '06/04/2019'
    assert volume[-1]['report_date'] == '06/10/2019'


@mark.asyncio
async def test_query_report(repository: Repository):
    async with server():
        report = await repository.query(date(2019, 6, 1), date(2019, 6, 10))

    assert len(report) == 14

    cutout = report[CutoutReport.Section.CUTOUT]
    assert len(cutout) == 6
    assert cutout[0]['report_date'] == '06/03/2019'
    assert cutout[1]['report_date'] == '06/04/2019'
    assert cutout[-1]['report_date'] == '06/10/2019'

    volume = report[CutoutReport.Section.VOLUME]
    assert len(volume) == 6
    assert volume[0]['report_date'] == '06/03/2019'
    assert volume[1]['report_date'] == '06/04/2019'
    assert volume[-1]['report_date'] == '06/10/2019'


@mark.asyncio
async def test_incremental_update(repository: Repository):
    async with server():
        await repository.query(date(2019, 6, 1), date(2019, 6, 10),
            CutoutReport.Section.CUTOUT, CutoutReport.Section.VOLUME)

        cutout = await repository.query(date(2019, 6, 1), date(2019, 6, 13), CutoutReport.Section.CUTOUT)

    assert len(cutout) == 9
    assert cutout[0]['report_date'] == '06/03/2019'
    assert cutout[-4]['report_date'] == '06/10/2019'
    assert cutout[-3]['report_date'] == '06/11/2019'
    assert cutout[-2]['report_date'] == '06/12/2019'
    assert cutout[-1]['report_date'] == '06/13/2019'
