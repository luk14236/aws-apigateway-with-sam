import behave_restful.app as br_app

from behave import given, when

@given(u'a custom url "{base_url}" and endpoint "{endpoint}"')
def step_impl(context, base_url, endpoint):
    context.request_url = context.config.userdata['base_url'] + endpoint
    context.request_headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'x-api-key': context.config.userdata.get('api_key')
    }