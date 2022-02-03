import pytest
from selenium import webdriver
USERNAME = "test_mail@test.ru"
PASSWORD = "your_password"

TIMESLEEP = 10
STARTPAGE = 'https://yandex.ru/'
message_header_text = 'Simbirsoft Тестовое задание\n'


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Remote('http://192.168.1.9:4444')
    yield browser
    browser.quit()
