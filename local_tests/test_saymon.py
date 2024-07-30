#!/usr/bin/env python
import time
from pages import settings
from pages import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_base(remote_browser):
    remote_browser.get(settings.test_url)
    assert WebDriverWait(remote_browser, 5).until(
        EC.presence_of_element_located((By.ID, locator.user_field)))
    remote_browser.find_element(By.ID, locator.user_field).send_keys(settings.valid_user)
    remote_browser.find_element(By.ID, locator.pass_field).send_keys(settings.valid_password)
    remote_browser.find_element(By.XPATH, locator.enter_btn).click()
    assert WebDriverWait(remote_browser, 5).until(
        EC.presence_of_element_located((By.XPATH, locator.logo_title)))
    assert remote_browser.current_url == settings.test_url
    assert 'SAYMON.SAAS' in remote_browser.page_source
    time.sleep(5)
    remote_browser.find_element(By.XPATH, locator.operation_launcher).click()
    assert ('Операция1' in remote_browser.find_element(By.XPATH, locator.last_operations).
            get_attribute('textContent'))
    assert (settings.valid_user in remote_browser.find_element(By.XPATH, locator.last_operations_user).
            get_attribute('textContent'))
    assert ('Test' in remote_browser.find_element(By.XPATH, locator.last_operations_result).
            get_attribute('textContent'))
    remote_browser.find_element(By.XPATH, locator.logout_0).click()
    remote_browser.find_element(By.XPATH, locator.logout_1).click()
    remote_browser.quit()
