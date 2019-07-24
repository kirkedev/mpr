Feature: Pork Cutout
  @pending
  Scenario: Morning Pork Cutout
    Given a date range from June 1st to June 30th, 2019
    When I request the daily pork cutout morning report
    Then I will receive a list of negotiated pork sales records as of 11:00am central time

  @pending
  Scenario: Afternoon Pork Cutout
    Given a date range from June 1st to June 30th, 2019
    When I request the daily pork cutout afternoon report
    Then I will receive a list of negotiated pork sales records as of 3:00pm central time
