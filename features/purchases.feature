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

  @pending
  Scenario: Daily Direct Hog Morning
    Given a date range from June 1st to June 30th, 2019
    When I request the daily direct hog morning report
    Then I will receive a list of daily hog purchase records as of 11:00am central time

  @pending
  Scenario: Daily Direct Hog Afternoon
    Given a date range from June 1st to June 30th, 2019
    When I request the daily direct hog afternoon report
    Then I will receive a list of daily hog purchase records as of 3:00pm central time
