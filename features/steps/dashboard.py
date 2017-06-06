from app.db import get_db
from app.entity.translation import TitleTranslation, TranslationStatus
from app.factory import create_app
from features.environment import fill_db

__author__ = 'Flavio Ferrara'

from behave import given, when, then

@given(u'the translation list is empty')
def step_impl(context):
    config = dict(
        DATABASE='empty_database',
        TESTING=True
    )
    app = create_app(config)
    context.client = app.test_client()

@when(u'user visit the dashboard')
def step_impl(context):
    context.rv = context.client.get('/dashboard', follow_redirects=True)

@then(u'no translation is displayed')
def step_impl(context):
    assert b'No entries here so far' in context.rv.data

@given(u'the translation list is not empty')
def step_impl(context):
    config = dict(
        DATABASE='test_db',
        TESTING=True
    )
    app = create_app(config)
    context.client = app.test_client()
    context.db, _ = get_db()
    fill_db(context.db)

    story = context.db.stories.find_one({'_id': 14499255})
    assert story['translations'][0]['status'] == TranslationStatus.PENDING
    assert story['translations'][1]['status'] == TranslationStatus.COMPLETED

@then(u'the translation jobs are displayed')
def step_impl(context):
    assert b'No entries here so far' not in context.rv.data
    assert context.rv.data.count(b'<li class="translation') > 0

@then(u'the unfinished translations are marked in yellow')
def step_impl(context):
    assert context.rv.data.count(b'translating') > 0
    assert context.rv.data.count(b'class="translation-machine_translate_in_progress"') > 0

@then(u'the finished translations are marked in green')
def step_impl(context):
    assert context.rv.data.count(b'translated') > 0
    assert context.rv.data.count(b'class="translation-deliver_ok"') > 0

