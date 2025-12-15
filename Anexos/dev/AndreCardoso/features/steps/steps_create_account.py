from behave import given, when, then

@given(u'I am a new user')
def step_impl(context):
    pass

@when(u'I create an account with user_id "{user_id}" and PIN "{pin}"')
def step_impl(context, user_id, pin):
    pass

@then(u'my account is created successfully')
def step_impl(context):
    pass

@then(u'my balance is {balance:d}')
def step_impl(context, balance):
    pass

@then(u'my PIN is securely stored')
def step_impl(context):
    pass

@when(u'I try to create an account with user_id "{user_id}" and PIN "{pin}"')
def step_impl(context, user_id, pin):
    pass

@then(u'account creation fails')
def step_impl(context):
    pass

@then(u'I receive an error message "{message}"')  # Este TEM parâmetro, diferente do comum
def step_impl(context, message):
    pass

@given(u'an account with user_id "{user_id}" already exists')
def step_impl(context, user_id):
    pass

@when(u'I create another account with user_id "{user_id}" and PIN "{pin}"')
def step_impl(context, user_id, pin):
    pass

@then(u'both accounts are created successfully')
def step_impl(context):
    pass

@then(u'the total number of accounts is {count:d}')
def step_impl(context, count):
    pass