Feature: Transfer Money to Other Users
  As a user
  I want to transfer money to other users
  So that I can send funds to friends and family

  Scenario: Successfully transfer money to another user
    Given I have an authenticated account
    And my wallet has a balance of 200.00 EUR
    And another user exists with ID "user123"
    When I transfer 50.00 EUR to user "user123"
    Then the transfer is successful
    And my wallet balance should be 150.00 EUR
    And user "user123" balance should increase by 50.00 EUR
    And I receive a confirmation message

  Scenario: Fail to transfer with insufficient funds
    Given I have an authenticated account
    And my wallet has a balance of 30.00 EUR
    And another user exists with ID "user123"
    When I transfer 50.00 EUR to user "user123"
    Then the transfer fails
    And I receive an insufficient funds error
    And my wallet balance should remain 30.00 EUR

  Scenario: Fail to transfer to non-existent user
    Given I have an authenticated account
    And my wallet has a balance of 100.00 EUR
    When I transfer 50.00 EUR to user "invalid_user"
    Then the transfer fails
    And I receive a user not found error
    And my wallet balance should remain 100.00 EUR

  Scenario: Fail to transfer negative amount
    Given I have an authenticated account
    And my wallet has a balance of 100.00 EUR
    And another user exists with ID "user123"
    When I transfer -10.00 EUR to user "user123"
    Then the transfer fails
    And I receive an invalid amount error
    And my wallet balance should remain 100.00 EUR

  Scenario: Fail to transfer without authentication
    Given I do not have an authenticated account
    When I transfer 50.00 EUR to user "user123"
    Then the transfer fails
    And I should receive an authentication error