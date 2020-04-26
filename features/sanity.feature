Feature: Sanity check

  Scenario: Application health is shown
    Given the app has a sanity check
    When I make a request
    Then I should get an "OK" message and "200" status code