from behave import given, when, then

@given(u'my wallet has a balance of {amount} EUR')
def step_impl(context, amount):
    pass

@when(u'I request to check my balance')
def step_impl(context):
    pass

@when(u'I complete a transaction of {amount} EUR')
def step_impl(context, amount):
    pass

@then(u'I should see my current balance is {amount} EUR')
def step_impl(context, amount):
    pass

@then(u'my balance should not be displayed')
def step_impl(context):
    pass