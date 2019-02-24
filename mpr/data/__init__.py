from enum import Enum


class Report(Enum):
    PURCHASED_SWINE = 'lm_hg200'
    SLAUGHTERED_SWINE = 'lm_hg201'
    DIRECT_HOG_MORNING = 'lm_hg202'
    DIRECT_HOG_AFTERNOON = 'lm_hg203'
    CUTOUT_MORNING = 'lm_pk602'
    CUTOUT_AFTERNOON = 'lm_pk603'
