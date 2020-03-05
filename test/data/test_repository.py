from datetime import date
from pathlib import Path

from pytest import fixture
from pytest import mark

from mpr.report import CutoutReport
from mpr.data.repository import Repository
from mpr.report import lm_pk602


@fixture
async def repository(tmp_path: Path):
    return Repository(lm_pk602, tmp_path)


@mark.asyncio
async def test_query_section(repository: Repository, mpr_server):
    async with mpr_server:
        cutout = await repository.query(date(2019, 5, 26), date(2019, 6, 6), CutoutReport.Section.CUTOUT)

    assert len(cutout) == 8
    assert cutout[0]['report_date'] == '05/28/2019'
    assert cutout[1]['report_date'] == '05/29/2019'
    assert cutout[-1]['report_date'] == '06/06/2019'


@mark.asyncio
async def test_query_sections(repository: Repository, mpr_server):
    async with mpr_server:
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
async def test_query_report(repository: Repository, mpr_server):
    async with mpr_server:
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
