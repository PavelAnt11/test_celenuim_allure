from Pages.base_page import BasePage
from .letter_page import LetterPage
from .locators import PostPageLocator
from conftest import message_header_text
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostPage(BasePage):
    def change_current_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def write_title_for_search(self):
        self.click_on_the_button(PostPageLocator.into_search_field)
        search_field = self.find_element_by_locator(PostPageLocator.find_all_message_with_title)
        search_field.send_keys(message_header_text)

    def open_only_input_letter(self):
        self.click_on_the_button(PostPageLocator.folders)
        self.click_on_the_button(PostPageLocator.inp)

    def should_be_input_letter(self):
        assert WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element(PostPageLocator.MessageSearch, 'в папке «Входящие»')), "Folder input doesn't open"

    def get_number_of_selected_letter(self):
        elem = self.find_element_by_locator(PostPageLocator.message_title)
        return elem.text

    def open_new_letter(self):
        self.click_on_the_button(PostPageLocator.button_write_letter)
        return LetterPage(browser=self.browser, url=self.browser.current_url)
