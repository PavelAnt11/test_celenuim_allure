from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Locator(object):
    # Google Search Page
    button_post = (By.CLASS_NAME, "desk-notif-card__login-new-item-title")
    text_area_id = (By.ID, "passp-field-login")
    button_enter = (By.ID, "passp:sign-in")
    text_area_passwrd = (By.ID, "passp-field-passwd")
    button_post_after_enter = (By.CLASS_NAME, "desk-notif-card__mail-title")
    incoming_messages = (By.XPATH, "//a[@data-title='Входящие']")
    into_search_field = (By.CLASS_NAME, "search-input__text-bubble-container")
    find_all_message_with_title = (By.CLASS_NAME, "textinput__control")
    button_search = (By.CLASS_NAME, "mail-MessagesSearchInfo-Title_misc")
    button_write_letter = (By.XPATH, "//a[@title='Написать (w, c)']")
    field_whom = (By.CLASS_NAME, "composeYabbles")
    field_header_letter = (By.CLASS_NAME, "composeTextField")
    field_body_letter_make_active = (By.CLASS_NAME, 'composeReact__main-content')
    field_body_letter = (By.CLASS_NAME, 'cke_wysiwyg_div')
    send_message = Keys.CONTROL + Keys.ENTER
