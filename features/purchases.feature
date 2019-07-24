Feature: Direct Hog Purchases
  Scenario: Daily Direct Hog Afternoon
    Given a date range from June 1st to June 30th, 2019
    When I request the daily direct hog prior day report
    Then I will receive a list of daily hog purchase records for the prior day
    | Report Date | Reported For Date | Purchase Type | Head Count | Price Range Low | Price Range High | Weighted Average Price |
    | 2019-06-04 | 2019-06-03 | Negotiated (carcass basis) | 9,502 | 68 | 78 | 76.11 |
    | 2019-06-04 | 2019-06-03 | Negotiated Formula (carcass basis) | 150 |  |  |  |
    | 2019-06-04 | 2019-06-03 | Combined Negotiated/Negotiated Formula (carcass basis) | 9,652 |  |  |  |
    | 2019-06-04 | 2019-06-03 | Swine/Pork Market Formula (carcass basis) | 118,892 | 71.39 | 83.42 | 78.74 |
    | 2019-06-04 | 2019-06-03 | Negotiated (live basis) | 139 |  |  |  |
    | 2019-06-04 | 2019-06-03 | Negotiated Formula (live basis) | 851 |  |  |  |
    | 2019-06-04 | 2019-06-03 | Combined Negotiated/Negotiated Formula (live basis) | 990 |  |  |  |
    | 2019-06-05 | 2019-06-04 | Negotiated Formula (live basis) | 1,007 |  |  |  |
    | 2019-06-05 | 2019-06-04 | Combined Negotiated/Negotiated Formula (live basis) | 1,829 |  |  |  |
    | 2019-06-05 | 2019-06-04 | Negotiated (live basis) | 822 | 56.85 | 62.5 | 59.75 |
    | 2019-06-05 | 2019-06-04 | Swine/Pork Market Formula (carcass basis) | 116,967 | 73.9 | 84.53 | 78.71 |
    | 2019-06-05 | 2019-06-04 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,647 |  |  |  |
    | 2019-06-05 | 2019-06-04 | Negotiated Formula (carcass basis) | 170 |  |  |  |
    | 2019-06-05 | 2019-06-04 | Negotiated (carcass basis) | 8,477 | 68 | 77 | 76.03 |
    | 2019-06-06 | 2019-06-05 | Negotiated (carcass basis) | 17,459 | 68 | 79 | 76.36 |
    | 2019-06-06 | 2019-06-05 | Negotiated Formula (carcass basis) | 490 |  |  |  |
    | 2019-06-06 | 2019-06-05 | Combined Negotiated/Negotiated Formula (carcass basis) | 17,949 |  |  |  |
    | 2019-06-06 | 2019-06-05 | Swine/Pork Market Formula (carcass basis) | 125,024 | 71.99 | 84.15 | 78.28 |
    | 2019-06-06 | 2019-06-05 | Negotiated (live basis) | 1,180 | 52.43 | 60.75 | 59.56 |
    | 2019-06-06 | 2019-06-05 | Combined Negotiated/Negotiated Formula (live basis) | 1,775 |  |  |  |
    | 2019-06-06 | 2019-06-05 | Negotiated Formula (live basis) | 595 |  |  |  |
    | 2019-06-07 | 2019-06-06 | Negotiated Formula (live basis) | 604 |  |  |  |
    | 2019-06-07 | 2019-06-06 | Combined Negotiated/Negotiated Formula (live basis) | 2,373 |  |  |  |
    | 2019-06-07 | 2019-06-06 | Negotiated (live basis) | 1,769 | 50.75 | 61.25 | 58.79 |
    | 2019-06-07 | 2019-06-06 | Swine/Pork Market Formula (carcass basis) | 118,542 | 71.61 | 83.92 | 78.14 |
    | 2019-06-07 | 2019-06-06 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,460 |  |  |  |
    | 2019-06-07 | 2019-06-06 | Negotiated Formula (carcass basis) | 490 |  |  |  |
    | 2019-06-07 | 2019-06-06 | Negotiated (carcass basis) | 7,970 | 68 | 77 | 75.58 |
    | 2019-06-10 | 2019-06-07 | Negotiated (carcass basis) | 8,505 | 67 | 76.5 | 75.89 |
    | 2019-06-10 | 2019-06-07 | Negotiated Formula (carcass basis) | 170 |  |  |  |
    | 2019-06-10 | 2019-06-07 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,675 |  |  |  |
    | 2019-06-10 | 2019-06-07 | Swine/Pork Market Formula (carcass basis) | 156,276 | 70.65 | 83.81 | 77.67 |
    | 2019-06-10 | 2019-06-07 | Negotiated (live basis) | 1,308 | 53.25 | 61 | 58.93 |
    | 2019-06-10 | 2019-06-07 | Combined Negotiated/Negotiated Formula (live basis) | 1,605 |  |  |  |
    | 2019-06-10 | 2019-06-07 | Negotiated Formula (live basis) | 297 |  |  |  |
    | 2019-06-11 | 2019-06-10 | Negotiated Formula (live basis) | 811 |  |  |  |
    | 2019-06-11 | 2019-06-10 | Combined Negotiated/Negotiated Formula (live basis) | 1,247 |  |  |  |
    | 2019-06-11 | 2019-06-10 | Negotiated (live basis) | 436 | 55 | 60 | 58.61 |
    | 2019-06-11 | 2019-06-10 | Swine/Pork Market Formula (carcass basis) | 108,614 | 72.44 | 82.03 | 77.81 |
    | 2019-06-11 | 2019-06-10 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,066 |  |  |  |
    | 2019-06-11 | 2019-06-10 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-11 | 2019-06-10 | Negotiated (carcass basis) | 4,906 | 67 | 76.5 | 74.7 |
    | 2019-06-12 | 2019-06-11 | Negotiated (carcass basis) | 13,189 | 67 | 77 | 75.2 |
    | 2019-06-12 | 2019-06-11 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-12 | 2019-06-11 | Combined Negotiated/Negotiated Formula (carcass basis) | 13,189 |  |  |  |
    | 2019-06-12 | 2019-06-11 | Swine/Pork Market Formula (carcass basis) | 124,872 | 71.7 | 83.2 | 77.47 |
    | 2019-06-12 | 2019-06-11 | Negotiated (live basis) | 1,053 | 51.5 | 61.15 | 58.61 |
    | 2019-06-12 | 2019-06-11 | Combined Negotiated/Negotiated Formula (live basis) | 1,323 |  |  |  |
    | 2019-06-12 | 2019-06-11 | Negotiated Formula (live basis) | 270 |  |  |  |
    | 2019-06-13 | 2019-06-12 | Negotiated Formula (live basis) | 328 |  |  |  |
    | 2019-06-13 | 2019-06-12 | Combined Negotiated/Negotiated Formula (live basis) | 1,604 |  |  |  |
    | 2019-06-13 | 2019-06-12 | Negotiated (live basis) | 1,276 | 55.5 | 60.5 | 59.31 |
    | 2019-06-13 | 2019-06-12 | Swine/Pork Market Formula (carcass basis) | 120,969 | 71.87 | 82.91 | 77.32 |
    | 2019-06-13 | 2019-06-12 | Combined Negotiated/Negotiated Formula (carcass basis) | 20,139 |  |  |  |
    | 2019-06-13 | 2019-06-12 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-13 | 2019-06-12 | Negotiated (carcass basis) | 19,979 | 68 | 78 | 76.07 |
    | 2019-06-14 | 2019-06-13 | Negotiated (carcass basis) | 8,660 | 67 | 78.25 | 75.83 |
    | 2019-06-14 | 2019-06-13 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-14 | 2019-06-13 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,820 |  |  |  |
    | 2019-06-14 | 2019-06-13 | Swine/Pork Market Formula (carcass basis) | 125,774 | 71.14 | 81.71 | 77.34 |
    | 2019-06-14 | 2019-06-13 | Negotiated (live basis) | 1,309 | 50 | 60.5 | 58.51 |
    | 2019-06-14 | 2019-06-13 | Combined Negotiated/Negotiated Formula (live basis) | 1,589 |  |  |  |
    | 2019-06-14 | 2019-06-13 | Negotiated Formula (live basis) | 280 |  |  |  |
    | 2019-06-17 | 2019-06-14 | Negotiated Formula (live basis) | 186 |  |  |  |
    | 2019-06-17 | 2019-06-14 | Combined Negotiated/Negotiated Formula (live basis) | 1,517 |  |  |  |
    | 2019-06-17 | 2019-06-14 | Negotiated (live basis) | 1,331 | 56 | 60.75 | 59.85 |
    | 2019-06-17 | 2019-06-14 | Swine/Pork Market Formula (carcass basis) | 129,902 | 71.33 | 82.82 | 77.48 |
    | 2019-06-17 | 2019-06-14 | Combined Negotiated/Negotiated Formula (carcass basis) | 13,065 |  |  |  |
    | 2019-06-17 | 2019-06-14 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-17 | 2019-06-14 | Negotiated (carcass basis) | 12,905 | 73 | 78 | 75.71 |
    | 2019-06-18 | 2019-06-17 | Negotiated (carcass basis) | 10,790 | 67 | 78 | 76.14 |
    | 2019-06-18 | 2019-06-17 | Negotiated Formula (carcass basis) | 170 |  |  |  |
    | 2019-06-18 | 2019-06-17 | Combined Negotiated/Negotiated Formula (carcass basis) | 10,960 |  |  |  |
    | 2019-06-18 | 2019-06-17 | Swine/Pork Market Formula (carcass basis) | 113,326 | 71.15 | 82.71 | 77.7 |
    | 2019-06-18 | 2019-06-17 | Negotiated (live basis) | 837 | 54 | 59.5 | 57.94 |
    | 2019-06-18 | 2019-06-17 | Combined Negotiated/Negotiated Formula (live basis) | 1,297 |  |  |  |
    | 2019-06-18 | 2019-06-17 | Negotiated Formula (live basis) | 460 |  |  |  |
    | 2019-06-19 | 2019-06-18 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-19 | 2019-06-18 | Combined Negotiated/Negotiated Formula (live basis) | 899 |  |  |  |
    | 2019-06-19 | 2019-06-18 | Negotiated (live basis) | 899 | 55 | 60.75 | 59.11 |
    | 2019-06-19 | 2019-06-18 | Swine/Pork Market Formula (carcass basis) | 116,998 | 71.3 | 82.52 | 77.49 |
    | 2019-06-19 | 2019-06-18 | Combined Negotiated/Negotiated Formula (carcass basis) | 15,554 |  |  |  |
    | 2019-06-19 | 2019-06-18 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-19 | 2019-06-18 | Negotiated (carcass basis) | 15,554 | 67 | 78 | 75.7 |
    | 2019-06-20 | 2019-06-19 | Negotiated (carcass basis) | 14,086 | 67 | 78.5 | 76.4 |
    | 2019-06-20 | 2019-06-19 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-20 | 2019-06-19 | Combined Negotiated/Negotiated Formula (carcass basis) | 14,086 |  |  |  |
    | 2019-06-20 | 2019-06-19 | Swine/Pork Market Formula (carcass basis) | 98,173 | 69.92 | 82.51 | 77.12 |
    | 2019-06-20 | 2019-06-19 | Negotiated (live basis) | 1,117 | 49.74 | 62 | 58.24 |
    | 2019-06-20 | 2019-06-19 | Combined Negotiated/Negotiated Formula (live basis) | 1,117 |  |  |  |
    | 2019-06-20 | 2019-06-19 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-21 | 2019-06-20 | Negotiated Formula (live basis) | 298 |  |  |  |
    | 2019-06-21 | 2019-06-20 | Combined Negotiated/Negotiated Formula (live basis) | 1,149 |  |  |  |
    | 2019-06-21 | 2019-06-20 | Negotiated (live basis) | 851 | 50 | 61.75 | 57.72 |
    | 2019-06-21 | 2019-06-20 | Swine/Pork Market Formula (carcass basis) | 135,847 | 67 | 82.74 | 76.68 |
    | 2019-06-21 | 2019-06-20 | Combined Negotiated/Negotiated Formula (carcass basis) | 4,126 |  |  |  |
    | 2019-06-21 | 2019-06-20 | Negotiated Formula (carcass basis) | 165 |  |  |  |
    | 2019-06-21 | 2019-06-20 | Negotiated (carcass basis) | 3,961 | 66 | 76 | 74.72 |
    | 2019-06-24 | 2019-06-21 | Negotiated (carcass basis) | 8,440 | 65 | 76 | 73.85 |
    | 2019-06-24 | 2019-06-21 | Negotiated Formula (carcass basis) | 52 |  |  |  |
    | 2019-06-24 | 2019-06-21 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,492 |  |  |  |
    | 2019-06-24 | 2019-06-21 | Swine/Pork Market Formula (carcass basis) | 137,042 | 65.53 | 82.99 | 76.66 |
    | 2019-06-24 | 2019-06-21 | Negotiated (live basis) | 1,729 | 50.75 | 60.75 | 57.51 |
    | 2019-06-24 | 2019-06-21 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-24 | 2019-06-21 | Combined Negotiated/Negotiated Formula (live basis) | 1,729 |  |  |  |
    | 2019-06-25 | 2019-06-24 | Combined Negotiated/Negotiated Formula (live basis) | 1,204 |  |  |  |
    | 2019-06-25 | 2019-06-24 | Negotiated Formula (live basis) | 165 |  |  |  |
    | 2019-06-25 | 2019-06-24 | Negotiated (live basis) | 1,039 | 54 | 59 | 58.1 |
    | 2019-06-25 | 2019-06-24 | Swine/Pork Market Formula (carcass basis) | 112,009 | 65.41 | 83.54 | 76.2 |
    | 2019-06-25 | 2019-06-24 | Combined Negotiated/Negotiated Formula (carcass basis) | 11,473 |  |  |  |
    | 2019-06-25 | 2019-06-24 | Negotiated Formula (carcass basis) | 155 |  |  |  |
    | 2019-06-25 | 2019-06-24 | Negotiated (carcass basis) | 11,318 | 63 | 75.5 | 73.51 |
    | 2019-06-26 | 2019-06-25 | Negotiated (carcass basis) | 8,962 | 62 | 76.5 | 72.07 |
    | 2019-06-26 | 2019-06-25 | Negotiated Formula (carcass basis) | 165 |  |  |  |
    | 2019-06-26 | 2019-06-25 | Combined Negotiated/Negotiated Formula (carcass basis) | 9,127 |  |  |  |
    | 2019-06-26 | 2019-06-25 | Swine/Pork Market Formula (carcass basis) | 118,202 | 68.02 | 82.4 | 75.28 |
    | 2019-06-26 | 2019-06-25 | Negotiated (live basis) | 961 | 50.28 | 60.95 | 57.68 |
    | 2019-06-26 | 2019-06-25 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-26 | 2019-06-25 | Combined Negotiated/Negotiated Formula (live basis) | 961 |  |  |  |
    | 2019-06-27 | 2019-06-26 | Combined Negotiated/Negotiated Formula (live basis) | 1,240 |  |  |  |
    | 2019-06-27 | 2019-06-26 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-27 | 2019-06-26 | Negotiated (live basis) | 1,240 | 53.5 | 59 | 56.09 |
    | 2019-06-27 | 2019-06-26 | Swine/Pork Market Formula (carcass basis) | 118,014 | 64.79 | 81.74 | 73.85 |
    | 2019-06-27 | 2019-06-26 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,944 |  |  |  |
    | 2019-06-27 | 2019-06-26 | Negotiated Formula (carcass basis) | 165 |  |  |  |
    | 2019-06-27 | 2019-06-26 | Negotiated (carcass basis) | 8,779 | 62 | 74.5 | 70.7 |
    | 2019-06-28 | 2019-06-27 | Negotiated (carcass basis) | 6,855 | 61 | 70.5 | 68.98 |
    | 2019-06-28 | 2019-06-27 | Negotiated Formula (carcass basis) | 200 |  |  |  |
    | 2019-06-28 | 2019-06-27 | Combined Negotiated/Negotiated Formula (carcass basis) | 7,055 |  |  |  |
    | 2019-06-28 | 2019-06-27 | Swine/Pork Market Formula (carcass basis) | 115,200 | 65.48 | 79.41 | 72.83 |
    | 2019-06-28 | 2019-06-27 | Negotiated (live basis) | 1,038 | 48 | 56.25 | 54.07 |
    | 2019-06-28 | 2019-06-27 | Negotiated Formula (live basis) | 168 |  |  |  |
    | 2019-06-28 | 2019-06-27 | Combined Negotiated/Negotiated Formula (live basis) | 1,206 |  |  |  |

  Scenario: Daily Direct Hog Morning
    Given a date range from June 1st to June 30th, 2019
    When I request the daily direct hog morning report
    Then I will receive a list of daily hog purchase records as of 11:00am central time
    | Report Date | Purchase Type | Head Count | Price Range Low | Price Range High | Weighted Average Price |
    | 2019-06-03 | Combined Negotiated/Negotiated Formula (live basis) | 1,340 |  |  |  |
    | 2019-06-03 | Negotiated Formula (live basis) | 590 |  |  |  |
    | 2019-06-03 | Negotiated (live basis) | 750 | 55.25 | 62.75 | 60.41 |
    | 2019-06-03 | Swine/Pork Market Formula (carcass basis) | 138,064 | 71.29 | 85.47 | 78.98 |
    | 2019-06-03 | Combined Negotiated/Negotiated Formula (carcass basis) | 2,784 |  |  |  |
    | 2019-06-03 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-03 | Negotiated (carcass basis) | 2,784 |  |  |  |
    | 2019-06-04 | Negotiated (carcass basis) | 7,012 | 68 | 78 | 75.96 |
    | 2019-06-04 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-04 | Combined Negotiated/Negotiated Formula (carcass basis) | 7,012 |  |  |  |
    | 2019-06-04 | Swine/Pork Market Formula (carcass basis) | 92,366 | 71.24 | 83.42 | 78.98 |
    | 2019-06-04 | Negotiated (live basis) | 451 |  |  |  |
    | 2019-06-04 | Negotiated Formula (live basis) | 842 |  |  |  |
    | 2019-06-04 | Combined Negotiated/Negotiated Formula (live basis) | 1,293 |  |  |  |
    | 2019-06-05 | Combined Negotiated/Negotiated Formula (live basis) | 990 |  |  |  |
    | 2019-06-05 | Negotiated Formula (live basis) | 595 |  |  |  |
    | 2019-06-05 | Negotiated (live basis) | 395 | 52.43 | 61.25 | 59.09 |
    | 2019-06-05 | Swine/Pork Market Formula (carcass basis) | 88,662 | 71.99 | 83.41 | 78.83 |
    | 2019-06-05 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,480 |  |  |  |
    | 2019-06-05 | Negotiated Formula (carcass basis) | 330 |  |  |  |
    | 2019-06-05 | Negotiated (carcass basis) | 8,150 | 68 | 76 | 75.61 |
    | 2019-06-06 | Negotiated (carcass basis) | 3,455 | 68 | 76 | 75.05 |
    | 2019-06-06 | Negotiated Formula (carcass basis) | 330 |  |  |  |
    | 2019-06-06 | Combined Negotiated/Negotiated Formula (carcass basis) | 3,785 |  |  |  |
    | 2019-06-06 | Swine/Pork Market Formula (carcass basis) | 91,625 | 71.61 | 84.15 | 78.74 |
    | 2019-06-06 | Negotiated (live basis) | 1,003 | 56 | 60.75 | 59.91 |
    | 2019-06-06 | Negotiated Formula (live basis) | 294 |  |  |  |
    | 2019-06-06 | Combined Negotiated/Negotiated Formula (live basis) | 1,297 |  |  |  |
    | 2019-06-07 | Combined Negotiated/Negotiated Formula (live basis) | 1,396 |  |  |  |
    | 2019-06-07 | Negotiated Formula (live basis) | 234 |  |  |  |
    | 2019-06-07 | Negotiated (live basis) | 1,162 |  |  |  |
    | 2019-06-07 | Swine/Pork Market Formula (carcass basis) | 95,786 | 71.77 | 82.57 | 78.24 |
    | 2019-06-07 | Combined Negotiated/Negotiated Formula (carcass basis) | 3,324 |  |  |  |
    | 2019-06-07 | Negotiated Formula (carcass basis) | 340 |  |  |  |
    | 2019-06-07 | Negotiated (carcass basis) | 2,984 | 68 | 77 | 74.8 |
    | 2019-06-10 | Negotiated (carcass basis) | 3,973 | 68 | 76.5 | 75.09 |
    | 2019-06-10 | Negotiated Formula (carcass basis) | 170 |  |  |  |
    | 2019-06-10 | Combined Negotiated/Negotiated Formula (carcass basis) | 4,143 |  |  |  |
    | 2019-06-10 | Swine/Pork Market Formula (carcass basis) | 112,924 | 71.37 | 83.81 | 78.16 |
    | 2019-06-10 | Negotiated (live basis) | 847 | 53.25 | 60.5 | 58.45 |
    | 2019-06-10 | Negotiated Formula (live basis) | 647 |  |  |  |
    | 2019-06-10 | Combined Negotiated/Negotiated Formula (live basis) | 1,494 |  |  |  |
    | 2019-06-11 | Combined Negotiated/Negotiated Formula (live basis) | 1,125 |  |  |  |
    | 2019-06-11 | Negotiated Formula (live basis) | 434 |  |  |  |
    | 2019-06-11 | Negotiated (live basis) | 691 | 56 | 61.15 | 59.14 |
    | 2019-06-11 | Swine/Pork Market Formula (carcass basis) | 80,070 | 71.7 | 82.03 | 78.23 |
    | 2019-06-11 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,100 |  |  |  |
    | 2019-06-11 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-11 | Negotiated (carcass basis) | 4,940 | 67 | 77 | 75.59 |
    | 2019-06-12 | Negotiated (carcass basis) | 7,122 | 67 | 77 | 74.74 |
    | 2019-06-12 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-12 | Combined Negotiated/Negotiated Formula (carcass basis) | 7,122 |  |  |  |
    | 2019-06-12 | Swine/Pork Market Formula (carcass basis) | 96,557 | 72.2 | 82.13 | 77.96 |
    | 2019-06-12 | Negotiated (live basis) | 285 | 56 | 60.5 | 57.8 |
    | 2019-06-12 | Negotiated Formula (live basis) | 328 |  |  |  |
    | 2019-06-12 | Combined Negotiated/Negotiated Formula (live basis) | 613 |  |  |  |
    | 2019-06-13 | Combined Negotiated/Negotiated Formula (live basis) | 1,192 |  |  |  |
    | 2019-06-13 | Negotiated Formula (live basis) | 280 |  |  |  |
    | 2019-06-13 | Negotiated (live basis) | 912 |  |  |  |
    | 2019-06-13 | Swine/Pork Market Formula (carcass basis) | 87,779 | 71.14 | 81.74 | 77.95 |
    | 2019-06-13 | Combined Negotiated/Negotiated Formula (carcass basis) | 3,207 |  |  |  |
    | 2019-06-13 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-13 | Negotiated (carcass basis) | 3,207 | 68 | 75.1 | 74.32 |
    | 2019-06-14 | Negotiated (carcass basis) | 6,890 | 67 | 76.75 | 75.69 |
    | 2019-06-14 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-14 | Combined Negotiated/Negotiated Formula (carcass basis) | 6,890 |  |  |  |
    | 2019-06-14 | Swine/Pork Market Formula (carcass basis) | 96,632 | 71.57 | 81.71 | 77.86 |
    | 2019-06-14 | Negotiated (live basis) | 1,028 | 51.5 | 60.5 | 58.81 |
    | 2019-06-14 | Negotiated Formula (live basis) | 186 |  |  |  |
    | 2019-06-14 | Combined Negotiated/Negotiated Formula (live basis) | 1,214 |  |  |  |
    | 2019-06-17 | Combined Negotiated/Negotiated Formula (live basis) | 971 |  |  |  |
    | 2019-06-17 | Negotiated Formula (live basis) | 295 |  |  |  |
    | 2019-06-17 | Negotiated (live basis) | 676 | 54 | 60.75 | 59.65 |
    | 2019-06-17 | Swine/Pork Market Formula (carcass basis) | 93,560 | 71.15 | 82.82 | 78.35 |
    | 2019-06-17 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,145 |  |  |  |
    | 2019-06-17 | Negotiated Formula (carcass basis) | 330 |  |  |  |
    | 2019-06-17 | Negotiated (carcass basis) | 4,815 | 67 | 76 | 74.7 |
    | 2019-06-18 | Negotiated (carcass basis) | 2,815 | 67 | 76 | 74.77 |
    | 2019-06-18 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-18 | Combined Negotiated/Negotiated Formula (carcass basis) | 2,815 |  |  |  |
    | 2019-06-18 | Swine/Pork Market Formula (carcass basis) | 84,163 | 71.3 | 81.96 | 78.23 |
    | 2019-06-18 | Negotiated (live basis) | 1,048 | 54.65 | 60.25 | 58.61 |
    | 2019-06-18 | Negotiated Formula (live basis) | 165 |  |  |  |
    | 2019-06-18 | Combined Negotiated/Negotiated Formula (live basis) | 1,213 |  |  |  |
    | 2019-06-19 | Combined Negotiated/Negotiated Formula (live basis) | 479 |  |  |  |
    | 2019-06-19 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-19 | Negotiated (live basis) | 479 | 55.11 | 60 | 57.46 |
    | 2019-06-19 | Swine/Pork Market Formula (carcass basis) | 82,619 | 72.71 | 82.45 | 78.1 |
    | 2019-06-19 | Combined Negotiated/Negotiated Formula (carcass basis) | 2,843 |  |  |  |
    | 2019-06-19 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-19 | Negotiated (carcass basis) | 2,843 | 67 | 75.14 | 74.66 |
    | 2019-06-20 | Negotiated (carcass basis) | 4,776 | 67 | 76 | 74.93 |
    | 2019-06-20 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-20 | Combined Negotiated/Negotiated Formula (carcass basis) | 4,776 |  |  |  |
    | 2019-06-20 | Swine/Pork Market Formula (carcass basis) | 92,306 | 69.92 | 82.51 | 77.1 |
    | 2019-06-20 | Negotiated (live basis) | 464 |  |  |  |
    | 2019-06-20 | Negotiated Formula (live basis) | 143 |  |  |  |
    | 2019-06-20 | Combined Negotiated/Negotiated Formula (live basis) | 607 |  |  |  |
    | 2019-06-21 | Combined Negotiated/Negotiated Formula (live basis) | 990 |  |  |  |
    | 2019-06-21 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-21 | Negotiated (live basis) | 990 | 50 | 61.75 | 57.08 |
    | 2019-06-21 | Swine/Pork Market Formula (carcass basis) | 96,259 | 67 | 82.72 | 76.69 |
    | 2019-06-21 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,191 |  |  |  |
    | 2019-06-21 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-21 | Negotiated (carcass basis) | 5,191 | 66 | 76 | 74.08 |
    | 2019-06-24 | Negotiated (carcass basis) | 4,118 | 64 | 75 | 72.32 |
    | 2019-06-24 | Negotiated Formula (carcass basis) | 52 |  |  |  |
    | 2019-06-24 | Combined Negotiated/Negotiated Formula (carcass basis) | 4,170 |  |  |  |
    | 2019-06-24 | Swine/Pork Market Formula (carcass basis) | 99,091 | 65.53 | 82.99 | 76.84 |
    | 2019-06-24 | Negotiated (live basis) | 1,350 | 50.75 | 60.73 | 57.22 |
    | 2019-06-24 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-24 | Combined Negotiated/Negotiated Formula (live basis) | 1,350 |  |  |  |
    | 2019-06-25 | Combined Negotiated/Negotiated Formula (live basis) | 193 |  |  |  |
    | 2019-06-25 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-25 | Negotiated (live basis) | 193 | 54 | 59 | 57.81 |
    | 2019-06-25 | Swine/Pork Market Formula (carcass basis) | 95,117 | 65.41 | 83.54 | 76.48 |
    | 2019-06-25 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,276 |  |  |  |
    | 2019-06-25 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-25 | Negotiated (carcass basis) | 5,276 | 63 | 75 | 71.92 |
    | 2019-06-26 | Negotiated (carcass basis) | 3,736 | 62 | 71.5 | 70.31 |
    | 2019-06-26 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-26 | Combined Negotiated/Negotiated Formula (carcass basis) | 3,736 |  |  |  |
    | 2019-06-26 | Swine/Pork Market Formula (carcass basis) | 90,427 | 64.79 | 82.4 | 74.68 |
    | 2019-06-26 | Negotiated (live basis) | 588 | 53.74 | 59 | 55.68 |
    | 2019-06-26 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-26 | Combined Negotiated/Negotiated Formula (live basis) | 588 |  |  |  |
    | 2019-06-27 | Combined Negotiated/Negotiated Formula (live basis) | 547 |  |  |  |
    | 2019-06-27 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-27 | Negotiated (live basis) | 547 | 53.88 | 57.25 | 55.56 |
    | 2019-06-27 | Swine/Pork Market Formula (carcass basis) | 89,383 | 65.48 | 80.99 | 73.56 |
    | 2019-06-27 | Combined Negotiated/Negotiated Formula (carcass basis) | 3,034 |  |  |  |
    | 2019-06-27 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-27 | Negotiated (carcass basis) | 3,034 | 62 | 71 | 69.11 |
    | 2019-06-28 | Negotiated (carcass basis) | 4,585 | 61 | 70 | 68 |
    | 2019-06-28 | Negotiated Formula (carcass basis) | 178 |  |  |  |
    | 2019-06-28 | Combined Negotiated/Negotiated Formula (carcass basis) | 4,763 |  |  |  |
    | 2019-06-28 | Swine/Pork Market Formula (carcass basis) | 90,939 | 65.02 | 79.41 | 72.44 |
    | 2019-06-28 | Negotiated (live basis) | 592 | 48 | 57 | 53.52 |
    | 2019-06-28 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-28 | Combined Negotiated/Negotiated Formula (live basis) | 592 |  |  |  |

  Scenario: Daily Direct Hog Afternoon
    Given a date range from June 1st to June 30th, 2019
    When I request the daily direct hog afternoon report
    Then I will receive a list of daily hog purchase records as of 3:00pm central time
    | Report Date | Purchase Type | Head Count | Price Range Low | Price Range High | Weighted Average Price |
    | 2019-06-03 | Combined Negotiated/Negotiated Formula (live basis) | 1,621 |  |  |  |
    | 2019-06-03 | Negotiated Formula (live basis) | 851 |  |  |  |
    | 2019-06-03 | Negotiated (live basis) | 770 | 55.25 | 62.75 | 60.38 |
    | 2019-06-03 | Swine/Pork Market Formula (carcass basis) | 164,606 | 71.29 | 85.47 | 78.81 |
    | 2019-06-03 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,055 |  |  |  |
    | 2019-06-03 | Negotiated Formula (carcass basis) | 150 |  |  |  |
    | 2019-06-03 | Negotiated (carcass basis) | 7,905 | 69 | 78 | 76.27 |
    | 2019-06-04 | Negotiated (carcass basis) | 10,159 | 68 | 78 | 75.98 |
    | 2019-06-04 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-04 | Combined Negotiated/Negotiated Formula (carcass basis) | 10,159 |  |  |  |
    | 2019-06-04 | Swine/Pork Market Formula (carcass basis) | 124,512 | 71.24 | 84.53 | 78.63 |
    | 2019-06-04 | Negotiated (live basis) | 592 | 58 | 62.5 | 59.73 |
    | 2019-06-04 | Negotiated Formula (live basis) | 1,007 |  |  |  |
    | 2019-06-04 | Combined Negotiated/Negotiated Formula (live basis) | 1,599 |  |  |  |
    | 2019-06-05 | Combined Negotiated/Negotiated Formula (live basis) | 1,120 |  |  |  |
    | 2019-06-05 | Negotiated Formula (live basis) | 595 |  |  |  |
    | 2019-06-05 | Negotiated (live basis) | 525 | 52.43 | 61.25 | 58.7 |
    | 2019-06-05 | Swine/Pork Market Formula (carcass basis) | 120,471 | 71.99 | 83.41 | 78.37 |
    | 2019-06-05 | Combined Negotiated/Negotiated Formula (carcass basis) | 18,224 |  |  |  |
    | 2019-06-05 | Negotiated Formula (carcass basis) | 490 |  |  |  |
    | 2019-06-05 | Negotiated (carcass basis) | 17,734 | 68 | 79 | 76.34 |
    | 2019-06-06 | Negotiated (carcass basis) | 7,670 | 68 | 77 | 75.63 |
    | 2019-06-06 | Negotiated Formula (carcass basis) | 490 |  |  |  |
    | 2019-06-06 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,160 |  |  |  |
    | 2019-06-06 | Swine/Pork Market Formula (carcass basis) | 119,539 | 71.61 | 84.15 | 78.39 |
    | 2019-06-06 | Negotiated (live basis) | 1,530 | 56 | 60.75 | 59.78 |
    | 2019-06-06 | Negotiated Formula (live basis) | 430 |  |  |  |
    | 2019-06-06 | Combined Negotiated/Negotiated Formula (live basis) | 1,960 |  |  |  |
    | 2019-06-07 | Combined Negotiated/Negotiated Formula (live basis) | 2,152 |  |  |  |
    | 2019-06-07 | Negotiated Formula (live basis) | 471 |  |  |  |
    | 2019-06-07 | Negotiated (live basis) | 1,681 | 50.75 | 61.25 | 58.87 |
    | 2019-06-07 | Swine/Pork Market Formula (carcass basis) | 130,374 | 70.65 | 82.57 | 77.68 |
    | 2019-06-07 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,230 |  |  |  |
    | 2019-06-07 | Negotiated Formula (carcass basis) | 340 |  |  |  |
    | 2019-06-07 | Negotiated (carcass basis) | 7,890 | 67 | 77 | 75.63 |
    | 2019-06-10 | Negotiated (carcass basis) | 5,158 | 67 | 76.5 | 75.27 |
    | 2019-06-10 | Negotiated Formula (carcass basis) | 170 |  |  |  |
    | 2019-06-10 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,328 |  |  |  |
    | 2019-06-10 | Swine/Pork Market Formula (carcass basis) | 143,601 | 71.37 | 83.81 | 77.8 |
    | 2019-06-10 | Negotiated (live basis) | 857 | 53.25 | 60.5 | 58.41 |
    | 2019-06-10 | Negotiated Formula (live basis) | 647 |  |  |  |
    | 2019-06-10 | Combined Negotiated/Negotiated Formula (live basis) | 1,504 |  |  |  |
    | 2019-06-11 | Combined Negotiated/Negotiated Formula (live basis) | 1,715 |  |  |  |
    | 2019-06-11 | Negotiated Formula (live basis) | 434 |  |  |  |
    | 2019-06-11 | Negotiated (live basis) | 1,281 | 56 | 61.15 | 59.26 |
    | 2019-06-11 | Swine/Pork Market Formula (carcass basis) | 110,812 | 71.7 | 83.2 | 77.5 |
    | 2019-06-11 | Combined Negotiated/Negotiated Formula (carcass basis) | 11,675 |  |  |  |
    | 2019-06-11 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-11 | Negotiated (carcass basis) | 11,515 | 67 | 77 | 75.3 |
    | 2019-06-12 | Negotiated (carcass basis) | 21,219 | 67 | 78 | 76.03 |
    | 2019-06-12 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-12 | Combined Negotiated/Negotiated Formula (carcass basis) | 21,379 |  |  |  |
    | 2019-06-12 | Swine/Pork Market Formula (carcass basis) | 129,422 | 71.87 | 82.91 | 77.42 |
    | 2019-06-12 | Negotiated (live basis) | 511 | 56 | 60.5 | 58.53 |
    | 2019-06-12 | Negotiated Formula (live basis) | 328 |  |  |  |
    | 2019-06-12 | Combined Negotiated/Negotiated Formula (live basis) | 839 |  |  |  |
    | 2019-06-13 | Combined Negotiated/Negotiated Formula (live basis) | 1,850 |  |  |  |
    | 2019-06-13 | Negotiated Formula (live basis) | 280 |  |  |  |
    | 2019-06-13 | Negotiated (live basis) | 1,570 | 50 | 60.1 | 59.14 |
    | 2019-06-13 | Swine/Pork Market Formula (carcass basis) | 121,346 | 71.14 | 81.74 | 77.3 |
    | 2019-06-13 | Combined Negotiated/Negotiated Formula (carcass basis) | 9,177 |  |  |  |
    | 2019-06-13 | Negotiated Formula (carcass basis) | 160 |  |  |  |
    | 2019-06-13 | Negotiated (carcass basis) | 9,017 | 67 | 78.25 | 75.75 |
    | 2019-06-14 | Negotiated (carcass basis) | 12,085 | 67 | 78 | 75.79 |
    | 2019-06-14 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-14 | Combined Negotiated/Negotiated Formula (carcass basis) | 12,085 |  |  |  |
    | 2019-06-14 | Swine/Pork Market Formula (carcass basis) | 125,734 | 71.33 | 81.71 | 77.25 |
    | 2019-06-14 | Negotiated (live basis) | 1,331 | 51.5 | 60.5 | 58.96 |
    | 2019-06-14 | Negotiated Formula (live basis) | 186 |  |  |  |
    | 2019-06-14 | Combined Negotiated/Negotiated Formula (live basis) | 1,517 |  |  |  |
    | 2019-06-17 | Combined Negotiated/Negotiated Formula (live basis) | 1,256 |  |  |  |
    | 2019-06-17 | Negotiated Formula (live basis) | 295 |  |  |  |
    | 2019-06-17 | Negotiated (live basis) | 961 | 54 | 60.75 | 59.23 |
    | 2019-06-17 | Swine/Pork Market Formula (carcass basis) | 122,845 | 71.15 | 82.82 | 77.8 |
    | 2019-06-17 | Combined Negotiated/Negotiated Formula (carcass basis) | 11,851 |  |  |  |
    | 2019-06-17 | Negotiated Formula (carcass basis) | 330 |  |  |  |
    | 2019-06-17 | Negotiated (carcass basis) | 11,521 | 67 | 78 | 76 |
    | 2019-06-18 | Negotiated (carcass basis) | 15,735 | 67 | 78 | 75.68 |
    | 2019-06-18 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-18 | Combined Negotiated/Negotiated Formula (carcass basis) | 15,735 |  |  |  |
    | 2019-06-18 | Swine/Pork Market Formula (carcass basis) | 111,595 | 71.3 | 82.52 | 77.66 |
    | 2019-06-18 | Negotiated (live basis) | 1,337 | 54.65 | 60.75 | 58.85 |
    | 2019-06-18 | Negotiated Formula (live basis) | 165 |  |  |  |
    | 2019-06-18 | Combined Negotiated/Negotiated Formula (live basis) | 1,502 |  |  |  |
    | 2019-06-19 | Combined Negotiated/Negotiated Formula (live basis) | 743 |  |  |  |
    | 2019-06-19 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-19 | Negotiated (live basis) | 743 | 49.74 | 62 | 58.11 |
    | 2019-06-19 | Swine/Pork Market Formula (carcass basis) | 99,536 | 70.68 | 82.45 | 77.61 |
    | 2019-06-19 | Combined Negotiated/Negotiated Formula (carcass basis) | 12,708 |  |  |  |
    | 2019-06-19 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-19 | Negotiated (carcass basis) | 12,708 | 67 | 78.5 | 76.49 |
    | 2019-06-20 | Negotiated (carcass basis) | 4,941 | 66 | 76 | 74.88 |
    | 2019-06-20 | Negotiated Formula (carcass basis) | 165 |  |  |  |
    | 2019-06-20 | Combined Negotiated/Negotiated Formula (carcass basis) | 5,106 |  |  |  |
    | 2019-06-20 | Swine/Pork Market Formula (carcass basis) | 126,554 | 69.92 | 82.74 | 76.96 |
    | 2019-06-20 | Negotiated (live basis) | 824 | 53.61 | 60.5 | 58.7 |
    | 2019-06-20 | Negotiated Formula (live basis) | 298 |  |  |  |
    | 2019-06-20 | Combined Negotiated/Negotiated Formula (live basis) | 1,122 |  |  |  |
    | 2019-06-21 | Combined Negotiated/Negotiated Formula (live basis) | 1,332 |  |  |  |
    | 2019-06-21 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-21 | Negotiated (live basis) | 1,332 | 50 | 61.75 | 57.54 |
    | 2019-06-21 | Swine/Pork Market Formula (carcass basis) | 131,060 | 67 | 82.72 | 76.44 |
    | 2019-06-21 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,216 |  |  |  |
    | 2019-06-21 | Negotiated Formula (carcass basis) | 0 |  |  |  |
    | 2019-06-21 | Negotiated (carcass basis) | 8,216 | 65 | 76 | 74.03 |
    | 2019-06-24 | Negotiated (carcass basis) | 10,963 | 64 | 75.5 | 73.51 |
    | 2019-06-24 | Negotiated Formula (carcass basis) | 207 |  |  |  |
    | 2019-06-24 | Combined Negotiated/Negotiated Formula (carcass basis) | 11,170 |  |  |  |
    | 2019-06-24 | Swine/Pork Market Formula (carcass basis) | 119,483 | 65.53 | 82.99 | 76.49 |
    | 2019-06-24 | Negotiated (live basis) | 1,870 | 50.75 | 60.73 | 57.56 |
    | 2019-06-24 | Negotiated Formula (live basis) | 165 |  |  |  |
    | 2019-06-24 | Combined Negotiated/Negotiated Formula (live basis) | 2,035 |  |  |  |
    | 2019-06-25 | Combined Negotiated/Negotiated Formula (live basis) | 901 |  |  |  |
    | 2019-06-25 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-25 | Negotiated (live basis) | 901 | 50.28 | 60.95 | 58.06 |
    | 2019-06-25 | Swine/Pork Market Formula (carcass basis) | 125,822 | 65.41 | 83.54 | 76.07 |
    | 2019-06-25 | Combined Negotiated/Negotiated Formula (carcass basis) | 9,916 |  |  |  |
    | 2019-06-25 | Negotiated Formula (carcass basis) | 165 |  |  |  |
    | 2019-06-25 | Negotiated (carcass basis) | 9,751 | 62 | 76.5 | 72.18 |
    | 2019-06-26 | Negotiated (carcass basis) | 8,441 | 62 | 74.5 | 70.68 |
    | 2019-06-26 | Negotiated Formula (carcass basis) | 165 |  |  |  |
    | 2019-06-26 | Combined Negotiated/Negotiated Formula (carcass basis) | 8,606 |  |  |  |
    | 2019-06-26 | Swine/Pork Market Formula (carcass basis) | 119,438 | 64.79 | 82.4 | 74.54 |
    | 2019-06-26 | Negotiated (live basis) | 1,089 | 53.5 | 59 | 55.88 |
    | 2019-06-26 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-26 | Combined Negotiated/Negotiated Formula (live basis) | 1,089 |  |  |  |
    | 2019-06-27 | Combined Negotiated/Negotiated Formula (live basis) | 1,045 |  |  |  |
    | 2019-06-27 | Negotiated Formula (live basis) | 168 |  |  |  |
    | 2019-06-27 | Negotiated (live basis) | 877 | 53.88 | 57.25 | 55.64 |
    | 2019-06-27 | Swine/Pork Market Formula (carcass basis) | 112,840 | 65.48 | 80.99 | 73.5 |
    | 2019-06-27 | Combined Negotiated/Negotiated Formula (carcass basis) | 7,074 |  |  |  |
    | 2019-06-27 | Negotiated Formula (carcass basis) | 40 |  |  |  |
    | 2019-06-27 | Negotiated (carcass basis) | 7,034 | 62 | 71 | 69.14 |
    | 2019-06-28 | Negotiated (carcass basis) | 7,055 | 61 | 70 | 68.18 |
    | 2019-06-28 | Negotiated Formula (carcass basis) | 268 | 69.7 | 72.82 | 71.61 |
    | 2019-06-28 | Combined Negotiated/Negotiated Formula (carcass basis) | 7,323 | 61 | 72.82 | 68.3 |
    | 2019-06-28 | Swine/Pork Market Formula (carcass basis) | 116,477 | 62.82 | 79.41 | 72.32 |
    | 2019-06-28 | Negotiated (live basis) | 942 | 48 | 57 | 53.96 |
    | 2019-06-28 | Negotiated Formula (live basis) | 0 |  |  |  |
    | 2019-06-28 | Combined Negotiated/Negotiated Formula (live basis) | 942 |  |  |  |
