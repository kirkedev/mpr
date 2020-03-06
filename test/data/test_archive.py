from datetime import date
from pathlib import Path

from isoweek import Week
from pytest import fixture

from mpr.data.archive import Archive
from mpr.report import CutoutReport


@fixture
async def archive(tmp_path: Path):
    report_date = date(2018, 8, 20)

    return Archive.create(tmp_path, Week.withdate(report_date), report_date,
    [{
        'slug': 'LM_PK602',
        'label': 'Cutout and Primal Values',
        'report_date': '08/20/2018',
        'pork_carcass': '67.18',
        'pork_loin': '75.51',
        'pork_butt': '89.55',
        'pork_picnic': '41.82',
        'pork_rib': '113.95',
        'pork_ham': '57.52',
        'pork_belly': '77.77'
    }, {
        'slug': 'LM_PK602',
        'label': 'Current Volume',
        'report_date': '08/20/2018',
        'temp_cuts_total_load': '334.74',
        'temp_process_total_load': '39.61'
    }])


def test_path(archive: Archive):
    assert Path(archive).name == "2018W34D00.zip"


def test_get_report_section(archive: Archive):
    assert len(archive.get(CutoutReport.Section.CUTOUT)) == 1


def test_get_multiple_sections(archive: Archive):
    cutout, volume = archive.get(CutoutReport.Section.CUTOUT, CutoutReport.Section.VOLUME)
    assert len(cutout) == 1
    assert len(volume) == 1


def test_get_full_report(archive: Archive):
    report = archive.get()
    assert len(report) == 2

    cutout = report[CutoutReport.Section.CUTOUT]
    assert len(cutout) == 1

    volume = report[CutoutReport.Section.VOLUME]
    assert len(volume) == 1


def test_update_archive(archive: Archive):
    archive.update(date(2018, 8, 21), [{
        'slug': 'LM_PK602',
        'label': 'Cutout and Primal Values',
        'report_date': '08/21/2018',
        'pork_carcass': '66.19',
        'pork_loin': '74.05',
        'pork_butt': '90.15',
        'pork_picnic': '40.61',
        'pork_rib': '115.35',
        'pork_ham': '55.92',
        'pork_belly': '76.45'
    }, {
        'slug': 'LM_PK602',
        'label': 'Current Volume',
        'report_date': '08/21/2018',
        'temp_cuts_total_load': '396.30',
        'temp_process_total_load': '52.57'
    }])
