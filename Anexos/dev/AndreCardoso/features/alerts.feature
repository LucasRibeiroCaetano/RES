Feature: Transaction Alerts

    As a user,
    I want to set spending limits,
    so that I am notified when I exceed them.

    Scenario: Receive alert
    Given I have set a transaction threshold
    When a transaction surpasses it
    Then I shall receive an alert notification

    Scenario: Set transaction threshold
    Given I have an account
    When I set a spending limit for that account
    Then A maximum transaction threshold is assigned to that account

