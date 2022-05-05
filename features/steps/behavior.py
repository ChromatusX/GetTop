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


@given('Open account page')
def open_account(context):
    context.app.main_page.open_url('/my-account/')


@then('Input valid email {email}')
def email_input(context, email):
    context.app.header.input_email(email)


@then('Input password {password}')
def pass_input(context, password):
    context.app.header.input_pass(password)


@then('Click login button')
def acc_click_login_button(context):
    context.app.header.account_login_button_click()


@then('Verify expected error message {message}')
def verify_acc_error_message(context, message):
    context.app.verification.verify_acc_error_message(message)


@given('Open lost password page')
def open_account(context):
    context.app.main_page.open_url('/my-account/lost-password/')


@then('Insert input {userinput} on lost password field')
def lost_pass_input(context, userinput):
    context.app.header.lost_pass_input(userinput)


@then('Click reset password button')
def reset_pass_button(context):
    context.app.header.click_reset_pass_button()


@then('Verify lost password error message {message}')
def verify_lost_pass_error_message(context, message):
    context.app.verification.verify_reset_pass_error_message(message)