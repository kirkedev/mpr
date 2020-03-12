from ..data.report import Section
from ..data.report import DailyReport


class DailyCutsReport(DailyReport):
    class Section(Section):
        LOIN = 'Loin Cuts'
        BUTT = 'Butt Cuts'
        PICNIC = 'Picnic Cuts'
        HAM = 'Ham Cuts'
        BELLY = 'Belly Cuts'
        RIB = 'Sparerib Cuts'
        JOWL = 'Jowl Cuts'
        TRIM = 'Trim Cuts'
        VARIETY = 'Variety Cuts'
        ADDED_INGREDIENT = 'Added Ingredient Cuts'


lm_pk602 = DailyCutsReport('lm_pk602', 'National Daily Pork - Negotiated Sales - Afternoon', 15)
