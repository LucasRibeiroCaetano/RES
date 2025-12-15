Feature: Link Payment Methods
  As a user
  I want to link a bank account or credit card to my wallet
  So that I can add funds and manage my payment methods

  Scenario: Successfully link a bank account
    Given I have an authenticated account
    When I provide valid bank account details
    Then the bank account is linked to my wallet
    And I receive a confirmation message

  Scenario: Successfully link a credit card
    Given I have an authenticated account
    When I provide valid credit card details
    Then the credit card is linked to my wallet
    And I receive a confirmation message

  Scenario: Fail to link invalid bank account
    Given I have an authenticated account
    When I provide invalid bank account details
    Then the bank account is not linked
    And I receive an error message

  Scenario: Fail to link invalid credit card
    Given I have an authenticated account
    When I provide invalid credit card details
    Then the credit card is not linked
    And I receive an error message