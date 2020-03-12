from ..data.report import DailyReport
from ..data.report import Section


class SlaughterReport(DailyReport):
    class Section(Section):
        SUMMARY = 'Summary'
        BARROWS_AND_GILTS = 'Barrows/Gilts'
        CARCASS_MEASUREMENTS = 'Carcass Measurements'
        SOWS_AND_BOARS = 'Sows/Boars'
        SCHEDULED_SWINE = '14-Day Scheduled Swine'
        NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'


lm_hg201 = SlaughterReport('lm_hg201', 'Daily Direct Hog Prior Day - Slaughtered Swine', 10)
