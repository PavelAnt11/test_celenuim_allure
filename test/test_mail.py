import allure
from Pages.start_page import StartPage
from conftest import STARTPAGE


@allure.severity('minor')
def test_start_page(browser, user_email, user_password):
    main_page = StartPage(browser, STARTPAGE)
    main_page.open()
    main_page.should_be_yandex_page()
    auth_page = main_page.open_authorization_page()
    auth_page.login_input(user_email)
    auth_page.should_be_valid_email()
    auth_page.password_input(user_password)
    auth_page.should_be_valid_password()
    post_page = main_page.open_post_page()
    post_page.change_current_window()
    post_page.write_title_for_search()
    post_page.open_only_input_letter()
    post_page.should_be_input_letter()
    text_body_letter = post_page.get_number_of_selected_letter()
    letter_page = post_page.open_new_letter()
    letter_page.enter_whom_send_letter(user_email)
    letter_page.enter_header_of_send_letter()
    letter_page.fill_in_body_of_letter(text_body_letter)
    letter_page.send_new_letter()
    letter_page.should_letter_be_sent()
