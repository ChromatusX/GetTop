from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open GetTop Page')
def open_getTop(context):
    context.app.main_page.open_main()


@when('Hover search icon')
def hover_search_icon(context):
    context.app.header.hover_search_icon()


@then('Search for item {item}')
def search_item(context, item):
    context.app.header.search_item(item)


@then('Verify message')
def verify_message(context):
    context.app.verification.verify_invalid_message()


@then('Verify item {item}')
def verify_items(context, item):
    context.app.verification.verify_item(item)
