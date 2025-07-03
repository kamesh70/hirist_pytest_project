# utils/locators.py
from selenium.webdriver.common.by import By


class DetailsPageLocators:

    def dynamic_xpath_using_a_tage(self,name):
        return (By.XPATH, f"//a[text()='{name}']")

