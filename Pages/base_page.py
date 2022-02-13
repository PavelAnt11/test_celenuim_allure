from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import TIMESLEEP


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_element_by_locator(self, locator, time=TIMESLEEP):
        return WebDriverWait(self.browser, time).\
            until(EC.presence_of_element_located(locator),
                  message=f"Нет такого элемента {locator}")

    def click_on_the_button(self, locator):
        return self.find_element_by_locator(locator).click()

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
