from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Header(Page):
    search_icon = (By.CSS_SELECTOR, "a[aria-label= 'Search' ]")
    search_bar = (By.ID, 'woocommerce-product-search-field-0')

    email_section = (By.ID, 'username')
    pass_section = (By.ID, 'password')
    account_login_button = (By.XPATH, "//button[@class='woocommerce-button button woocommerce-form-login__submit']")

    lost_pass_input_field = (By.ID, 'user_login')
    reset_password_button = (By.XPATH, "//button[@class='woocommerce-Button button']")

    def hover_search_icon(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.search_icon))
        actions.perform()

    def search_item(self, item):
        bar = self.driver.find_element(*self.search_bar)
        bar.send_keys(item, Keys.RETURN)
        sleep(2)

    def input_email(self, email):
        email_input = self.driver.find_element(*self.email_section)
        email_input.send_keys(email)

    def input_pass(self, password):
        pass_input = self.driver.find_element(*self.pass_section)
        pass_input.send_keys(password)

    def account_login_button_click(self):
        logButton = self.driver.find_element(*self.account_login_button)
        logButton.click()

    def lost_pass_input(self, userinput):
        field = self.driver.find_element(*self.lost_pass_input_field)
        field.send_keys(userinput)

    def click_reset_pass_button(self):
        resetButton = self.driver.find_element(*self.reset_password_button)
        resetButton.click()