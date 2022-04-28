from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Header(Page):
    search_icon = (By.CSS_SELECTOR, "a[aria-label= 'Search' ]")
    search_bar = (By.ID, 'woocommerce-product-search-field-0')

    def hover_search_icon(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.search_icon))
        actions.perform()

    def search_item(self, item):
        bar = self.driver.find_element(*self.search_bar)
        bar.send_keys(item, Keys.RETURN)
        sleep(2)