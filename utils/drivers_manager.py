# utils/drivers_manager.py
from selenium import webdriver

def get_driver(browser: str):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver
