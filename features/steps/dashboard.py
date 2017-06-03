__author__ = 'Flavio Ferrara'

from behave import given, when, then

@given(u'the translation list is empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the translation list is empty')

@when(u'user visit the dashboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user visit the dashboard')

@then(u'no translation is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then no translation is displayed')

@given(u'the translation list is not empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the translation list is not empty')

@then(u'the translation jobs are displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the translation jobs are displayed')

@given(u'the translation list contain some unfinished job')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the translation list contain some unfinished job')

@then(u'the unfinished translations are marked in yellow')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the unfinished translations are marked in yellow')

@given(u'the translation list contain some finished job')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the translation list contain some finished job')

@then(u'the finished translations are marked in green')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the finished translations are marked in green')

