from behave import *
from api import main


@given(u'the app has a sanity check')
def step_impl(context):
	main.app.config['TESTING'] = True


@when(u'I make a request')
def step_impl(context):
	with main.app.test_client() as client:
		context.response = client.get('/')


@then(u'I should get an "OK" message and "200" status code')
def step_impl(context):
	assert b'{"message": "ok"}' in context.response.data.splitlines()


@given(u'I have the client_id "client_id_example"')
def step_impl(context):
	raise NotImplementedError(u'STEP: Given I have the client_id "client_id_example"')


@given(u'the user "user_test"')
def step_impl(context):
	raise NotImplementedError(u'STEP: Given the user "user_test"')


@when(u'I send a request using "/login"')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I send a request using "/login"')


@then(u'I should get a token')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should get a token')
