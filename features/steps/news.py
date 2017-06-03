from app.factory import create_app

__author__ = 'Flavio Ferrara'

from behave import given, when, then

def init_db():
    return None

@given(u'the news list is empty')
def step_impl(context):
    config = dict(
        DATABASE='empty_database',
        TESTING=True
    )
    app = create_app(config)
    context.client = app.test_client()

@when(u'user visit the homepage')
def step_impl(context):
    context.rv = context.client.get('/', follow_redirects=True)

@then(u'no post is displayed')
def step_impl(context):
    assert b'No entries here so far' in context.rv.data

@given(u'the news list contain at least 10 news')
def step_impl(context):
    config = dict(
        DATABASE='test_db',
        TESTING=True
    )
    app = create_app(config)
    context.client = app.test_client()

@then(u'10 news are displayed')
def step_impl(context):
    assert b'No entries here so far' not in context.rv.data
    assert context.rv.data.count(b'<li class="story') == 10

@when(u'user visit the homepage in italian')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user visit the homepage in italian')

@then(u'the news titles are in italian')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the news titles are in italian')

@when(u'user visit the homepage in pt-br')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user visit the homepage in pt-br')

@then(u'the news titles are in pt-br')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the news titles are in pt-br')

