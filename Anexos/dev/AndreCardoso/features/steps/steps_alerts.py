from behave import given, when, then

# REMOVIDO: @given('I have an account')

@given('I have set a transaction threshold')
def step_impl(context):
    pass

@when('a transaction surpasses it')
def step_impl(context):
    pass

@then('I shall receive an alert notification')
def step_impl(context):
    pass

@when('I set a spending limit for that account')
def step_impl(context):
    pass

@then('A maximum transaction threshold is assigned to that account')
def step_impl(context):
    pass