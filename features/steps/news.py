__author__ = 'Flavio Ferrara'

from behave import given, when, then

@given(u'the news list is empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the news list is empty')

@when(u'user visit the homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user visit the homepage')

@then(u'no post is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then no post is displayed')

@given(u'the news list contain at least 10 news')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the news list contain at least 10 news')

@then(u'10 news are displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then 10 news are displayed')

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

