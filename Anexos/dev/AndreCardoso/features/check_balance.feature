Feature: Check Wallet Balance
  As a user
  I want to check my wallet balance
  So that I can know how much money I have available

  Scenario: Successfully check balance with funds
    Given I have an authenticated account
    And my wallet has a balance of 100.00 EUR
    When I request to check my balance
    Then I should see my current balance is 100.00 EUR

  Scenario: Check balance with zero funds
    Given I have an authenticated account
    And my wallet has a balance of 0.00 EUR
    When I request to check my balance
    Then I should see my current balance is 0.00 EUR

  Scenario: Check balance without authentication
    Given I do not have an authenticated account
    When I request to check my balance
    Then I should receive an authentication error
    And my balance should not be displayed

  Scenario: Check balance after transaction
    Given I have an authenticated account
    And my wallet has a balance of 150.00 EUR
    When I complete a transaction of 50.00 EUR
    And I request to check my balance
    Then I should see my current balance is 100.00 EUR