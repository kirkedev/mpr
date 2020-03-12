from ..data.report import DailyReport
from ..data.report import Section


class PurchaseReport(DailyReport):
    class Section(Section):
        VOLUME = 'Current Volume by Purchase Type'
        BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
        CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
        CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
        AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
        SOWS = 'Sows'
        STATES = 'State of Origin'


lm_hg200 = PurchaseReport('lm_hg200', 'Daily Direct Hog Prior Day - Purchased Swine', 8)
lm_hg202 = PurchaseReport('lm_hg202', 'Daily Direct Hog - Morning', 11)
lm_hg203 = PurchaseReport('lm_hg203', 'Daily Direct Hog - Afternoon', 15)
