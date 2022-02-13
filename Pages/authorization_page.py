from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import AuthorizationPageLocator


class AuthorizationPage(BasePage):

    def enter_text(self, locator, word):
        search_field = self.find_element_by_locator(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def login_input(self, user_email):
        self.enter_text(AuthorizationPageLocator.text_area_id, user_email)
        self.click_on_the_button(AuthorizationPageLocator.button_enter)

    def should_be_valid_email(self):
        assert self.is_not_element_present(*AuthorizationPageLocator.error_login),\
            "Your email isn't correct"

    def password_input(self, password):
        self.enter_text(AuthorizationPageLocator.text_area_passwrd, password)
        self.click_on_the_button(AuthorizationPageLocator.button_enter)
        return None

    def should_be_valid_password(self):
        assert self.is_not_element_present(*AuthorizationPageLocator.error_paswd), \
            "Invalid password"
