Feature: Cash Purchases
  @pending
  Scenario: June Purchases
    Given a date range from June 1st to June 30th, 2019
    When I request the purchases report
    Then I will receive a report of prior day lean hog purchases from June 2019
