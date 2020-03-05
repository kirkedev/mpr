from datetime import date
from pathlib import Path

from isoweek import Week
from pytest import fixture

from mpr.data.archive import Archive
from mpr.report import CutoutReport


@fixture
async def archive(tmp_path: Path):
    archive = Archive(tmp_path, Week.withdate(date(2018, 8, 20)))

    archive.save({
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

    return archive


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
