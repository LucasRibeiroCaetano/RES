from behave import given, when, then

@given(u'I have an authenticated account')
def step_impl(context):
    pass

@given(u'I do not have an authenticated account')
def step_impl(context):
    pass

@given(u'I have an account')
def step_impl(context):
    pass

@then(u'I receive a confirmation message')
def step_impl(context):
    pass

@then(u'I receive an error message')
def step_impl(context):
    pass

@then(u'I should receive an authentication error')
def step_impl(context):
    pass