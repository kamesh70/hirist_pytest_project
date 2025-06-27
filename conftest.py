import logging

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from config.config_page import EMAIL,PASSWORD

@pytest.fixture
def driver():
    driver= webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.hirist.tech/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Fixture to log in before tests requiring authentication."""
    logging.info("Logging in before test execution")
    login_page = LoginPage(driver)
    login_page.driver_login(EMAIL,PASSWORD) # Use valid credentials
    return driver  # Return the driver in logged-in state
