Feature: Sanity check

  Scenario: Application health is shown
    Given the app has a sanity check
    When I make a request
    Then I should get an "OK" message and "200" status code

  Scenario: Sending client_id to GitHub to get authorization
    Given I have the client_id "client_id_example"
    And the user "user_test"
    When I send a request using "/login"
    Then I should get a token