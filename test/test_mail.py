from selenium.webdriver.common.by import By
import pytest
import allure
import time
from PageObject import StartPage, YandexMail
# blocker , critical, normal, minor, trivial

USERNAME = "demariohermann@yandex.ru"
PASSWORD = "sfdfAKP3jmJ8CBr"




@allure.feature('Открытие страницы')
@allure.story('Открываем стартовую yandex')
@allure.severity('blocker')
def test_startpage(browser):
    main_page = YandexMail(browser)
    page = main_page.get_site()
    assert main_page.browser.title == 'Яндекс'

@allure.feature('Открытие страницы')
@allure.story('Открываем стартовую почты')
def test_login(browser):
    main_page = YandexMail(browser)
    main_page.click_on_the_button((By.CLASS_NAME, "desk-notif-card__login-new-item-title"))
    assert 1

@allure.feature('Ввод данных')
@allure.story('Вводим логин')
def test_input_login(browser):
    main_page = YandexMail(browser)
    main_page.enter_text((By.ID, "passp-field-login"), USERNAME)
    main_page.click_on_the_button((By.ID, "passp:sign-in"))
    assert 1

@allure.feature('Ввод данных')
@allure.story('Вводим пароль')
def test_input_pass(browser):
    main_page = YandexMail(browser)
    main_page.enter_text((By.ID, "passp-field-passwd"), PASSWORD)
    main_page.click_on_the_button((By.ID, "passp:sign-in"))
    assert 1

@allure.feature('Переход на страницу')
@allure.story('Переход в почту')
def test_go_to_mail(browser):
    main_page = YandexMail(browser)
    """После входа открывается стартовая и нам нужно перейти в саму почту"""
    main_page.click_on_the_button((By.CLASS_NAME, "desk-notif-card__mail-title"))
    time.sleep(10) #  Дожидаемся загрузки всех писем
    main_page.browser.switch_to.window(browser.window_handles[1])  # меням активную вкладку
    assert 1

def test_go_to_input_message(browser):
    main_page = YandexMail(browser)
    elem = main_page.find_element((By.XPATH, "//a[@data-title='Входящие']"))
    elem.click()
    assert 1

def test_find_all_need_mess(browser):
    main_page = YandexMail(browser)
    main_page.click_on_the_button((By.CLASS_NAME, "search-input__text-bubble-container"))
    main_page.enter_text((By.CLASS_NAME, "textinput__control"),'Simbirsoft Тестовое задание\n')
    time.sleep(5)
    num = main_page.find_element((By.CLASS_NAME, "mail-MessagesSearchInfo-Title_misc"))
    browser.num = num.text
    assert 1


@allure.feature('Пишем новое сообщение')
def test_create_new_mail(browser):
    main_page = YandexMail(browser)
    main_page.click_on_the_button((By.XPATH, "//a[@title='Написать (w, c)']"))
    assert 1

@allure.feature('Заполняем поля нового сообщения')
def test_fill_in_field(browser):
    main_page = YandexMail(browser)
    main_page.enter_text((By.CLASS_NAME, "composeYabbles"), USERNAME)
    main_page.enter_text((By.CLASS_NAME, "composeTextField"), 'Simbirsoft Тестовое задание, Антюфеев.')
    main_page.click_on_the_button((By.CLASS_NAME, 'composeReact__main-content'))
    last2 = main_page.enter_text((By.CLASS_NAME, 'cke_wysiwyg_div'), str(browser.num))
    main_page.send_message(last2)
    assert 1

# pytest --alluredir results
# allure serv results
# pip freeze > requirements.txt

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
