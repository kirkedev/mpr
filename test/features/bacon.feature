Feature: CME Fresh Bacon Index
  Scenario: June 2019 Fresh Bacon Index
    Given a date range from June 1st to June 30th, 2019
    When I request the CME fresh bacon index
    Then I will receive a report of fresh bacon prices from June 2019
    | Date | Bacon Index | Index Change | Total Weight | Negotiated Price | Negotiated Weight | Formula Price | Formula Weight |
    | 2019-06-07 | 143.20 | -10.00 | 17785025 | 128.62 | 2710194 | 145.82 | 15074831 |
    | 2019-06-14 | 139.66 |  -3.54 | 17811995 | 125.92 | 2778143 | 142.19 | 15033852 |
    | 2019-06-21 | 137.73 |  -1.93 | 18691599 | 123.20 | 3114614 | 140.64 | 15576985 |
    | 2019-06-28 | 134.02 |  -3.71 | 13780350 | 121.46 | 1682623 | 135.77 | 12097727 |
