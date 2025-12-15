Feature: User Authentication
  As a registered user
  I want to authenticate securely
  So that I can access my wallet

  Scenario: Successful login with correct PIN
    Given I have an account with user_id "user001" and PIN "1234"
    When I login with user_id "user001" and PIN "1234"
    Then I am authenticated successfully
    And I can access my wallet

  Scenario: Failed login with wrong PIN
    Given I have an account with user_id "user001" and PIN "1234"
    When I login with user_id "user001" and PIN "9999"
    Then authentication fails
    And I receive an error message "Invalid PIN"
    And my wrong attempt counter increases

  Scenario: Account locked after 3 failed attempts
    Given I have an account with user_id "user001" and PIN "1234"
    When I login with user_id "user001" and wrong PIN 3 times
    Then my account is locked
    And I receive an error message "Account locked due to multiple failed attempts"

  Scenario: Cannot login with locked account
    Given my account with user_id "user001" is locked
    When I try to login with user_id "user001" and correct PIN "1234"
    Then authentication fails
    And I receive an error message "Account is locked"

  Scenario: Reset wrong attempts after successful login
    Given I have an account with user_id "user001" and PIN "1234"
    And I have 2 wrong login attempts
    When I login with user_id "user001" and PIN "1234"
    Then I am authenticated successfully
    And my wrong attempt counter is reset to 0