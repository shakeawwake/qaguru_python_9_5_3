import pytest
from selene.support.shared import browser, config
from selenium import webdriver

@pytest.fixture(scope="function")
def start_settings_google():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    config.window_width = 1920
    config.window_height = 1080

    yield
    browser.quit()