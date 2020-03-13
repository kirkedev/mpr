from enum import IntEnum
from typing import Dict
from typing import Iterator

from .report import SalesReport
from ..data.report import Section


class Cut(IntEnum):
    LOIN = 1
    BUTT = 2
    PICNIC = 3
    HAM = 4
    BELLY = 5
    RIB = 6
    JOWL = 7
    TRIM = 8
    VARIETY = 9
    ADDED_INGREDIENT = 10


cut_types: Dict[str, Cut] = {
    'Loin Cuts': Cut.LOIN,
    'Butt Cuts': Cut.BUTT,
    'Picnic Cuts': Cut.PICNIC,
    'Ham Cuts': Cut.HAM,
    'Belly Cuts': Cut.BELLY,
    'Sparerib Cuts': Cut.RIB,
    'Jowl Cuts': Cut.JOWL,
    'Trim Cuts': Cut.TRIM,
    'Variety Cuts': Cut.VARIETY,
    'Added Ingredient Cuts': Cut.ADDED_INGREDIENT
}


def report_sections(*cuts: Cut) -> Iterator[Section]:
    return (SalesReport.Section(key) for key, value in cut_types.items() if value in cuts)
