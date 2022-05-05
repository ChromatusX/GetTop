from pages.base_page import Page
from selenium.webdriver.common.by import By


class Verification(Page):
    invalid_message = (By.XPATH, "//p[@class='woocommerce-info']")
    items_shown = (By.XPATH, "//p[@class='category uppercase is-smaller no-text-overflow product-cat op-7']")

    account_error_message = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")
    lost_pass_error_message = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")

    def verify_invalid_message(self):
        actual_result = self.driver.find_element(*self.invalid_message).text
        expected_result = 'No products were found matching your selection.'

        assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"

    def verify_item(self, item):
        actual_result = self.driver.find_element(*self.items_shown).text
        expected_result = item.upper()
        assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"

    def verify_acc_error_message(self, message):
        actual_result = self.driver.find_element(*self.account_error_message).text
        print(actual_result)
        expected_result = message
        assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"

    def verify_reset_pass_error_message(self, message):
        actual_result = self.driver.find_element(*self.lost_pass_error_message).text
        print(actual_result)
        expected_result = message
        assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
