import pytest
from selenium import webdriver

TIMESLEEP = 10
STARTPAGE = 'https://yandex.ru/'
message_header_text = 'Simbirsoft Тестовое задание\n'


def pytest_addoption(parser):
    parser.addoption('--email', action='store')
    parser.addoption('--password', action='store')


@pytest.fixture
def user_email(request):
    return request.config.getoption("--email")


@pytest.fixture
def user_password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Remote('http://192.168.1.48:4444')
    yield browser
    browser.quit()
