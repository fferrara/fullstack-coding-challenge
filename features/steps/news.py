from app.db import get_db
from app.factory import create_app
from features.environment import fill_db

__author__ = 'Flavio Ferrara'

from behave import given, when, then

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

@given(u'the news list contains some news')
def step_impl(context):
    config = dict(
        DATABASE='test_db',
        TESTING=True
    )
    app = create_app(config)
    context.client = app.test_client()
    db, _ = get_db(app)
    fill_db(db)

@then(u'the news are displayed')
def step_impl(context):
    assert b'No entries here so far' not in context.rv.data
    assert context.rv.data.count(b'<li class="story') > 0

@when(u'user visit the homepage in italian')
def step_impl(context):
    context.rv = context.client.get('/stories?lang=it', follow_redirects=True)

@then(u'the news titles are in italian')
def step_impl(context):
    assert b'Mostra HN: Monica, un CRM open source per gestire amici e familiari' in context.rv.data

@when(u'user visit the homepage in pt')
def step_impl(context):
    context.rv = context.client.get('/stories?lang=pt', follow_redirects=True)

@then(u'the news titles are in pt')
def step_impl(context):
    assert b'Mostrar HN: Monica, um CRM open-source para gerenciar amigos e familiares' in context.rv.data