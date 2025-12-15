from behave import given, when, then

@when(u'I provide valid bank account details')
def step_impl(context):
    pass

@when(u'I provide valid credit card details')
def step_impl(context):
    pass

@when(u'I provide invalid bank account details')
def step_impl(context):
    pass

@when(u'I provide invalid credit card details')
def step_impl(context):
    pass

@then(u'the bank account is linked to my wallet')
def step_impl(context):
    pass

@then(u'the credit card is linked to my wallet')
def step_impl(context):
    pass

@then(u'the bank account is not linked')
def step_impl(context):
    pass

@then(u'the credit card is not linked')
def step_impl(context):
    pass