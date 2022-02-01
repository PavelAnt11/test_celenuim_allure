import pytest
from selenium import webdriver

USERNAME = "demariohermann@yandex.ru"
PASSWORD = "sfdfAKP3jmJ8CBr"


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Remote('http://192.168.1.9:4444')
    yield browser
    browser.quit()
