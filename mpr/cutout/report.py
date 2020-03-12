from ..data.report import DailyReport
from ..data.report import Section


class CutoutReport(DailyReport):
    class Section(Section):
        CUTOUT = 'Cutout and Primal Values'
        DAILY_CHANGE = 'Change From Prior Day'
        FIVE_DAY_AVERAGE = '5-Day Average Cutout and Primal Values'
        VOLUME = 'Current Volume'
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


lm_pk600 = CutoutReport('lm_pk600', 'National Daily Pork - Negotiated Sales - Morning', 11)
lm_pk602 = CutoutReport('lm_pk602', 'National Daily Pork - Negotiated Sales - Afternoon', 15)
