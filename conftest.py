import pytest
from selenium import webdriver
from selenium.webdriver import Remote


def pytest_addoption(parser):
    """Parse pytest --option variables from shell"""
    parser.addoption('--browser', help='Which test browser?',
                     default='chrome')


@pytest.fixture(scope='session')
def test_browser(request):
    """returns Browser.NAME from --browser option"""
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def remote_browser(test_browser) -> Remote:
    driver = webdriver.Remote(
        options=webdriver.ChromeOptions(),
        command_executor='http://192.168.3.78:4444/wd/hub'
    )
    driver.set_window_size(1920, 1080)
    return driver
