from enum import IntEnum
from typing import Dict


class CutType(IntEnum):
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


cut_types: Dict[str, CutType] = {
    'Loin Cuts': CutType.LOIN,
    'Butt Cuts': CutType.BUTT,
    'Picnic Cuts': CutType.PICNIC,
    'Ham Cuts': CutType.HAM,
    'Belly Cuts': CutType.BELLY,
    'Sparerib Cuts': CutType.RIB,
    'Jowl Cuts': CutType.JOWL,
    'Trim Cuts': CutType.TRIM,
    'Variety Cuts': CutType.VARIETY,
    'Added Ingredient Cuts': CutType.ADDED_INGREDIENT
}
