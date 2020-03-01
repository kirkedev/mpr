from typing import Iterator
from datetime import date

from numpy import float32

from ..api import Attributes
from ..api import fetch
from ..api import filter_sections
from ..date import from_string
from ..report import CutoutReport

from .model import Cutout

date_format = "%m/%d/%Y"


def parse_attributes(cutout: Attributes, volume: Attributes) -> Cutout:
    report_date = from_string(cutout['report_date'], date_format)

    return Cutout(
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
    response = await fetch(report, start, end)

    return map(lambda it: parse_attributes(*it),
        filter_sections(response, report.Section.CUTOUT, report.Section.VOLUME))
