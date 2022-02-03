import pytest
import allure
from PageObjectFolder.Locators import Locator
from PageObjectFolder.PageObject import YandexMail
from PageObjectFolder.conftest import message_header_text, USERNAME, PASSWORD, browser


@allure.feature('Открытие страницы')
@allure.story('Открываем стартовую yandex')
@allure.severity('blocker')
def test_start_page(browser):
    main_page = YandexMail(browser)
    main_page.get_site()
    assert main_page.browser.title == 'Яндекс'

    main_page.click_on_the_button(Locator.button_post)
    main_page.enter_text(Locator.text_area_id, USERNAME)
    main_page.click_on_the_button(Locator.button_enter)

    main_page.enter_text(Locator.text_area_passwrd, PASSWORD)
    main_page.click_on_the_button(Locator.button_enter)

    main_page.click_on_the_button(Locator.button_post_after_enter)
    main_page.browser.switch_to.window(browser.window_handles[1])

    main_page.click_on_the_button(Locator.incoming_messages)

    main_page.click_on_the_button(Locator.into_search_field)
    main_page.enter_text(Locator.find_all_message_with_title, message_header_text)

    text_body_letter = main_page.find_element(Locator.button_search)
    text_body_letter = text_body_letter.text  # В этой переменной количество найденных писем с нашей темой

    main_page.click_on_the_button(Locator.button_write_letter)

    main_page.enter_text(Locator.field_whom, USERNAME)
    main_page.enter_text(Locator.field_header_letter, 'Simbirsoft Тестовое задание, Антюфеев.')
    main_page.click_on_the_button(Locator.field_body_letter_make_active)
    letter = main_page.enter_text(Locator.field_body_letter, text_body_letter)
    letter.send_keys(Locator.send_message)


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
