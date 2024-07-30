import pytest
from selenium import webdriver


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    driver = webdriver.Chrome('./chrome-linux64/chrome')
    browser.set_window_size(1920, 1080)

    yield browser

