Feature: Transfer Money between Users
  As a verified user,
  I want to securely transfer money to another user,
  so that I can pay friends or family instantly.

  Background:
    # Set up initial state with generic user placeholders
    Given a user "Alice" with account ID "A001" and balance of 100.00
    And a user "Bob" with account ID "B002" and balance of 50.00
    And "Alice" is logged in

  Scenario: Successful Transfer
    When "Alice" transfers 25.00 to "Bob"
    Then the transfer should be successful
    # Use generic steps with placeholders
    And "Alice"'s balance should be 75.00
    And "Bob"'s balance should be 75.00
    And a transaction record is created

  Scenario: Insufficient Funds
    When "Alice" attempts to transfer 150.00 to "Bob"
    Then the transfer should fail with an "Insufficient Funds" error
    # Use generic steps with placeholders to check that the balance is unchanged
    And "Alice"'s balance should remain 100.00
    And "Bob"'s balance should remain 50.00

  Scenario: Invalid Recipient
    When "Alice" attempts to transfer 10.00 to an invalid recipient "C003"
    Then the transfer should fail with an "Invalid Recipient" error
    # Use generic steps with placeholders
    And "Alice"'s balance should remain 100.00
    And "Bob"'s balance should remain 50.00