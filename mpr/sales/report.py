from ..data.report import DailyReport
from ..data.report import Section
from ..data.report import WeeklyReport


class SalesReport:
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


class DailySalesReport(DailyReport, SalesReport):
    pass


class WeeklySalesReport(WeeklyReport, SalesReport):
    pass


lm_pk602 = DailySalesReport('lm_pk602', 'National Daily Pork Report - Negotiated Sales', hour=15)
lm_pk610 = WeeklySalesReport('lm_pk610', 'National Weekly Pork Report - Negotiated Sales', weekday=4, hour=16)
lm_pk620 = WeeklySalesReport('lm_pk620', 'National Weekly Pork Report - Formula Sales', weekday=0, hour=10)
