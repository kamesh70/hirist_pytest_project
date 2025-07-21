#conftest.py

import pytest,logging
from config.config_manager import ConfigManager
from pages.login_page import LoginPage
from config.config_page import EMAIL,PASSWORD
from utils.drivers_manager import get_driver

@pytest.fixture
def driver():
    logging.info("Starting WebDriver")
    config = ConfigManager.get_config()
    browser = config.get("browser")  # 'chrome' or 'firefox' or browser = config.get("browser", "firefox")
    base_url = config.get("base_url")   #  or  base_url = config.get("base_url", "https://default-url.com")

    driver = get_driver(browser)  # ✅ instantiate WebDriver here
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(base_url)

    yield driver
    logging.info("Quitting WebDriver")
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Fixture to log in before tests requiring authentication."""
    logging.info("Logging in before test execution")
    login_page = LoginPage(driver)
    login_page.driver_login(EMAIL,PASSWORD) # Use valid credentials
    return driver  # Return the driver in logged-in state


# Configure logging
LOG_FILE = "test_log.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)