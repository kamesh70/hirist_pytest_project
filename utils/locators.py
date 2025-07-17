# utils/locators.py
from selenium.webdriver.common.by import By


class DetailsPageLocators:

    user_image=(By.XPATH,"//div[@class='MuiBox-root mui-style-wvhck8']")
    edit_path =(By.XPATH,"//p[text()='EDIT']")
    play_store_path=(By.XPATH,"//a[text()='Get the hirist app']")
    assert_profile=(By.XPATH,"//li[text()='Profile']")




    def dynamic_xpath_using_a_tage(self,name):
        return (By.XPATH, f"//li/a[text()='{name}']")

