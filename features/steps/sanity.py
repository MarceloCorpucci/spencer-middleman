from behave import *
from api import main


@given(u'the app has a sanity check')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the app has a sanity check')


@when(u'I make a request')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I make a request')


@then(u'I should get an "OK" message and "200" status code')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get an "OK" message and "200" status code')
