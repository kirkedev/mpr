from ..data.report import Section
from ..data.report import DailyReport
from .. data.report import WeeklyReport


class CutsReport:
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


class DailyCutsReport(DailyReport, CutsReport):
    pass


class WeeklyCutsReport(WeeklyReport, CutsReport):
    pass


lm_pk602 = DailyCutsReport('lm_pk602', 'National Daily Pork - Negotiated Sales - Afternoon', hour=15)
lm_pk620 = WeeklyCutsReport('lm_pk620', 'National Weekly Pork Report - Formula Sales', weekday=0, hour=10)
