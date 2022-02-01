from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class StartPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://yandex.ru/'

    def get_site(self):
        return self.browser.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Нет такого элемента {locator}")


class YandexMail(StartPage):
    def enter_text(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_button(self, locator):
        return self.find_element(locator, time=2).click()

    def send_message(self, fill):
        fill.send_keys(Keys.CONTROL + Keys.ENTER)
