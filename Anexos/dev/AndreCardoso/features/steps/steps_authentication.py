from behave import given, when, then

@given(u'I have an account with user_id "{user_id}" and PIN "{pin}"')
def step_impl(context, user_id, pin):
    pass

@when(u'I login with user_id "{user_id}" and PIN "{pin}"')
def step_impl(context, user_id, pin):
    pass

@then(u'I am authenticated successfully')
def step_impl(context):
    pass

@then(u'I can access my wallet')
def step_impl(context):
    pass

@then(u'authentication fails')
def step_impl(context):
    pass

@then(u'my wrong attempt counter increases')
def step_impl(context):
    pass

@when(u'I login with user_id "{user_id}" and wrong PIN {attempts:d} times')
def step_impl(context, user_id, attempts):
    pass

@then(u'my account is locked')
def step_impl(context):
    pass

@given(u'my account with user_id "{user_id}" is locked')
def step_impl(context, user_id):
    pass

@when(u'I try to login with user_id "{user_id}" and correct PIN "{pin}"')
def step_impl(context, user_id, pin):
    pass

@given(u'I have {attempts:d} wrong login attempts')
def step_impl(context, attempts):
    pass

@then(u'my wrong attempt counter is reset to {count:d}')
def step_impl(context, count):
    pass