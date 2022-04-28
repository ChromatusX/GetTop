from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@given('Open GetTop Page')
def open_getTop(context):
    context.driver.get('https://gettop.us/')


@then('Hover search icon')
def hover_search_icon(context):
    actions = ActionChains(context.driver)
    actions.move_to_element((context.driver.find_element(By.CSS_SELECTOR, "a[aria-label= 'Search' ]")))
    actions.perform()


@then('Search for item {item}')
def search_valid(context, item):
    context.driver.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys(f"{item}", Keys.RETURN)
    sleep(1)


@then('Verify message')
def verify_message(context):
    actual_result = context.driver.find_element(By.XPATH, "//p[@class='woocommerce-info']").text
    expected_result = 'No products were found matching your selection.'

    assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"


@then('Verify item {item}')
def verify_items(context, item):
    actual_result = context.driver.find_element(By.XPATH, "//p[@class='category uppercase is-smaller no-text-overflow product-cat op-7']").text
    expected_result = f"{item}".upper()
    print(expected_result)
    assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
