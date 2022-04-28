from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://gettop.us/'
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, end_url: str = ''):  #default it to empty string
        self.driver.get(f'{self.base_url}{end_url}')

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))