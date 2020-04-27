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
