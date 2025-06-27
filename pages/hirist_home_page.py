from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HiristHomePage(BasePage):
    jobseeker_path =(By.XPATH, "//button/p[text()='Jobseeker Login']")

    def click_jobseeker_button(self):
        self.click(self.jobseeker_path)



