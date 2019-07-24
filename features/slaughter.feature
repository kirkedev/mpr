Feature: Slaughtered Swine
  @pending
  Scenario: Prior Day Slaughtered Swine
    Given a date range from June 1st to June 30th, 2019
    When I request the daily slaughtered swine report
    Then I will receive a list of slaughtered swine records for the prior day
