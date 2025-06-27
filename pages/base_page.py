import logging
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, StaleElementReferenceException)
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    timeout = 20  # Default timeout

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.actions =ActionChains( self.driver)

    def capture_screenshot(self, screenshot_name="screenshot"):
        """Capture a screenshot and save it with the given name."""
        screenshots_folder = "screenshots"
        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshots_folder, f"{screenshot_name}_{timestamp}.png")
        try:
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved at: {screenshot_path}")
        except Exception as e:
            logging.error(f"Failed to capture screenshot: {e}")

    def move_element(self,element):
        ele = self.element_visible(element)
        self.actions.move_to_element(ele)
        self.actions.perform()

    def element_visible(self,locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logging.error(f"element{locator} not found {e}")
            self.capture_screenshot("element_visible_base_page_function")
        return None


    def find_element(self, locator):
        """Wait for an element to be present and return it."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Element {locator} not found: {e}")
            self.capture_screenshot("find_element_failure")
        return None

    def find_elements(self, locator):
        """Wait for multiple elements to be present and return them."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException as e:
            logging.error(f"Elements {locator} not found: {e}")
            self.capture_screenshot("find_elements_failure")
        return []

    def click(self, locator):
        """Click on an element after ensuring it's visible and interactable."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logging.info(f"Clicked on element: {locator}")
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            logging.error(f"Error clicking {locator}: {e}")
            print(f"click button error {locator}")

            self.capture_screenshot("click_failure")
            if isinstance(e, StaleElementReferenceException):
                logging.warning(f"Retrying click for {locator}")
                self.click(locator)  # Retry clicking the element

    @property
    def current_page_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator) )
            return element.text.strip()
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving text from {locator}: {e}")
            self.capture_screenshot("get_text_failure")
        return None

    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text: '{text}' in element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error entering text into {locator}: {e}")
            self.capture_screenshot("enter_text_failure")

    def wait_for_page_load(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def wait_find_element(self,locator):
        return self.wait.until(lambda d:d.find_element(*locator))

    def wait_find_elements(self,locator):
        return self.wait.until(lambda d:d.find_elements(*locator))
