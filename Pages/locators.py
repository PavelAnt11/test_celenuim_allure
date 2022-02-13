from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class StartPageLocator:
    button_enter = (By.CSS_SELECTOR,
                    "a.desk-notif-card__login-new-item:nth-child(1) > div:nth-child(2)")
    button_post_after_enter = (By.CLASS_NAME, "desk-notif-card__mail-title")


class AuthorizationPageLocator:
    text_area_id = (By.ID, "passp-field-login")
    error_login = (By.ID, "field:input-login:hint")
    error_paswd = (By.ID, "field:input-passwd:hint")
    button_enter = (By.ID, "passp:sign-in")
    text_area_passwrd = (By.ID, "passp-field-passwd")


class PostPageLocator:
    into_search_field = (By.CLASS_NAME, "search-input__text-bubble-container")
    find_all_message_with_title = (By.CLASS_NAME, "textinput__control")
    folders = (By.CSS_SELECTOR, "button.button2_size_l:nth-child(3)")
    inp = (By.CSS_SELECTOR, 'div.control:nth-child(1) > span:nth-child(1)')
    MessageSearch = (By.CLASS_NAME, "mail-MessagesSearchInfo_Summary")
    message_title = (By.CLASS_NAME, "mail-MessagesSearchInfo-Title_misc")
    button_write_letter = (By.XPATH, "//a[@title='Написать (w, c)']")


class LetterPageLocator:
    field_whom = (By.CLASS_NAME, "composeYabbles")
    field_header_letter = (By.CLASS_NAME, "composeTextField")
    field_body_letter_make_active = (By.CLASS_NAME, 'composeReact__main-content')
    field_body_letter = (By.CLASS_NAME, 'cke_wysiwyg_div')
    send_message = Keys.CONTROL + Keys.ENTER
    send = (By.CSS_SELECTOR, ".Button2_view_default")
    success_message = (By.CLASS_NAME, 'ComposeDoneScreen-Title')
