from itertools import starmap
from typing import Iterator
from datetime import date

from numpy import float32

from ..date import from_string
from ..report import CutoutReport
from ..data.api import Record
from ..data.repository import Repository

from .model import Cutout

date_format = "%m/%d/%Y"


def parse_record(cutout: Record, volume: Record) -> Cutout:
    report_date = from_string(cutout['report_date'], date_format)

    return Cutout(
        report=cutout['slug'].lower(),
        date=report_date,
        report_date=report_date,
        primal_loads=float32(volume['temp_cuts_total_load']),
        trimming_loads=float32(volume['temp_process_total_load']),
        carcass_price=float32(cutout['pork_carcass']),
        loin_price=float32(cutout['pork_loin']),
        butt_price=float32(cutout['pork_butt']),
        picnic_price=float32(cutout['pork_picnic']),
        rib_price=float32(cutout['pork_rib']),
        ham_price=float32(cutout['pork_ham']),
        belly_price=float32(cutout['pork_belly']))


async def fetch_cutout(report: CutoutReport, start: date, end=date.today()) -> Iterator[Cutout]:
    cutout, volume = await Repository(report).query(start, end, report.Section.CUTOUT, report.Section.VOLUME)
    return starmap(parse_record, zip(cutout, volume))
