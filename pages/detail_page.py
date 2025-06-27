import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DetailPage(BasePage):
    search_icon_path = (By.XPATH,"//div[@data-testid='search_icon']")
    verify_search=(By.XPATH,"//p[text()='Search for Jobs, Companies, Courses']")
    search_page_title_path =(By.XPATH,"//p[contains(@class,'mui-style-bzxy8k')]")


    def search_fun(self):
        self.click(self.search_icon_path)
        return self.get_text(self.search_page_title_path).strip()


