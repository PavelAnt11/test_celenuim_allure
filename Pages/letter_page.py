from Pages.base_page import BasePage
from .locators import LetterPageLocator


class LetterPage(BasePage):
    def enter_whom_send_letter(self, user_email):
        whom_field = self.find_element_by_locator(LetterPageLocator.field_whom)
        whom_field.send_keys(user_email)

    def enter_header_of_send_letter(self):
        self.click_on_the_button(LetterPageLocator.field_header_letter)
        header_field = self.find_element_by_locator(
            LetterPageLocator.field_header_letter)
        header_field.send_keys('Simbirsoft Тестовое задание, Антюфеев.')

    def fill_in_body_of_letter(self, text_body):
        self.click_on_the_button(LetterPageLocator.field_body_letter_make_active)
        body_field = self.find_element_by_locator(
            LetterPageLocator.field_body_letter)
        body_field.send_keys(text_body)

    def send_new_letter(self):
        self.click_on_the_button(LetterPageLocator.send)

    def should_letter_be_sent(self):
        mes = self.find_element_by_locator(LetterPageLocator.success_message)
        assert "Письмо отправлено" in mes.text
