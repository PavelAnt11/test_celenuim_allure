from Pages.authorization_page import AuthorizationPage
from Pages.base_page import BasePage
from .locators import StartPageLocator
from .post_page import PostPage


class StartPage(BasePage):

    def open(self):
        self.browser.get(self.url)

    def should_be_yandex_page(self):
        assert self.browser.title == 'Яндекс', "Site isn't Yandex"

    def open_authorization_page(self):
        self.click_on_the_button(StartPageLocator.button_enter)
        return AuthorizationPage(browser=self.browser, url=self.browser.current_url)

    def open_post_page(self):
        self.click_on_the_button(StartPageLocator.button_post_after_enter)
        return PostPage(browser=self.browser, url=self.browser.current_url)
