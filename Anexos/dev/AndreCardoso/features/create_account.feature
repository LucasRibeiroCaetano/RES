Feature: Create User Account
  As a new user
  I want to create an account
  So that I can use the digital wallet

  Scenario: Successfully create account with valid PIN
    Given I am a new user
    When I create an account with user_id "user001" and PIN "1234"
    Then my account is created successfully
    And my balance is 0
    And my PIN is securely stored

  Scenario: Fail to create account with short PIN
    Given I am a new user
    When I try to create an account with user_id "user002" and PIN "12"
    Then account creation fails
    And I receive an error message "PIN must be 4 digits"

  Scenario: Fail to create duplicate account
    Given an account with user_id "user003" already exists
    When I try to create an account with user_id "user003" and PIN "5678"
    Then account creation fails
    And I receive an error message "User already exists"

  Scenario: Create multiple accounts
    Given I am a new user
    When I create an account with user_id "user004" and PIN "1111"
    And I create another account with user_id "user005" and PIN "2222"
    Then both accounts are created successfully
    And the total number of accounts is 2