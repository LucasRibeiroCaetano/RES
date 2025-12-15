from behave import given, when, then, register_type
from decimal import Decimal
import parse

# --- Type Converter for Financial Precision ---
@parse.with_pattern(r"\d+\.\d{2}")
def parse_decimal(text):
    """Converts the step text to a Decimal object for accurate financial calculations."""
    return Decimal(text)

register_type(Decimal=parse_decimal)

# --- GIVEN Steps ---

# This single step definition handles ALL user initializations (Alice, Bob, etc.)
@given('a user "{user_name}" with account ID "{user_id}" and balance of {initial_balance:Decimal}')
def step_impl_initial_balance(context, user_name, user_id, initial_balance):
    # Set up the initial state for the user.
    pass

@given('"{user_name}" is logged in')
def step_impl_user_logged_in(context, user_name):
    # Check the Precondition: User is authenticated.
    pass

# --- WHEN Steps ---

@when('"{sender_name}" transfers {amount:Decimal} to "{recipient_name}"')
def step_impl_transfer(context, sender_name, amount, recipient_name):
    # Execute the core transfer function (UC1 Main Flow).
    pass

@when('"{sender_name}" attempts to transfer {amount:Decimal} to "{recipient_name}"')
def step_impl_attempt_transfer(context, sender_name, amount, recipient_name):
    # Execute the transfer function but expect it to fail (e.g., Insufficient Funds).
    pass

@when('"{sender_name}" attempts to transfer {amount:Decimal} to an invalid recipient "{recipient_id}"')
def step_impl_invalid_recipient(context, sender_name, amount, recipient_id):
    # Tests validation logic (UC1 Main Flow Step 2).
    pass

# --- THEN Steps ---

@then('the transfer should be successful')
def step_impl_successful(context):
    # Assert that the system executed the transfer without exceptions.
    pass

# This single step definition handles ALL balance checks (e.g., Alice's balance is 75.00, Bob's balance remains 50.00)
@then('"{user_name}"\'s balance should be {expected_balance:Decimal}')
def step_impl_check_balance(context, user_name, expected_balance):
    # Verify the Postcondition: Balances updated.
    pass

# This single step definition handles the check when the balance remains unchanged (used in failed scenarios)
@then('"{user_name}"\'s balance should remain {expected_balance:Decimal}')
def step_impl_check_balance_remains(context, user_name, expected_balance):
    # Alias for the generic balance check, used when a transaction fails.
    pass

@then('the transfer should fail with an "{error_message}" error')
def step_impl_transfer_failed(context, error_message):
    # Verifies that the expected failure condition was met.
    pass

@then('a transaction record is created')
def step_impl_record_created(context):
    # Verify the Postcondition: Transaction record created.
    pass