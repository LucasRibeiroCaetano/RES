from behave import given, when, then

@given(u'another user exists with ID "{user_id}"')
def step_impl(context, user_id):
    pass

@when(u'I transfer {amount} EUR to user "{user_id}"')
def step_impl(context, amount, user_id):
    pass

@then(u'the transfer is successful')
def step_impl(context):
    pass

@then(u'the transfer fails')
def step_impl(context):
    pass

@then(u'my wallet balance should be {amount} EUR')
def step_impl(context, amount):
    pass

@then(u'my wallet balance should remain {amount} EUR')
def step_impl(context, amount):
    pass

@then(u'user "{user_id}" balance should increase by {amount} EUR')
def step_impl(context, user_id, amount):
    pass

@then(u'I receive an insufficient funds error')
def step_impl(context):
    pass

@then(u'I receive a user not found error')
def step_impl(context):
    pass

@then(u'I receive an invalid amount error')
def step_impl(context):
    pass