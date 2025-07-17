from selenium.webdriver.common.by import By


def link_by__li_a_text(text):
    return (By.XPATH, f"//li/a[text()='{text}']")

def link_by_a_text(text):
    return (By.XPATH, f"//a[text()='{text}']")


def paragraph_by_text(text):
    return (By.XPATH, f"//p[text()='{text}']")


def button_by_text(text):
    return (By.XPATH, f"//button[normalize-space(text())='{text}']")


def input_by_placeholder(placeholder):
    return (By.XPATH, f"//input[@placeholder='{placeholder}']")


def label_for_input(label_text):
    return (By.XPATH, f"//label[contains(text(), '{label_text}')]/following-sibling::input")




""" how to use this method in  pages file  """
# from utils.dynamic_locators import link_by_text
#
# class DetailsPage:
#     def click_skill_link(self, skill_name):
#         skill_locator = link_by_text(skill_name)
#         self.driver.find_element(*skill_locator).click()
