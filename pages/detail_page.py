import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DetailPage(BasePage):
    search_icon_path = (By.XPATH,"//div[@data-testid='search_icon']")
    verify_search=(By.XPATH,"//p[text()='Search for Jobs, Companies, Courses']")
    search_page_title_path =(By.XPATH,"//p[contains(@class,'mui-style-bzxy8k')]")
    notification_path=(By.XPATH,"//span[contains(@class,'MuiBadge-root mui-style-x0z9yr')]")
    open_notification=(By.XPATH,"//p[contains(@class,'mui-style-9npega')]")
    show_all_notification=(By.XPATH,"//a[contains(@class,'mui-style-1eo38lg')]")
    text_verify_path =(By.XPATH,"//p[contains(@class,'mui-style-15fxu1t')]")


    def search_fun(self):
        self.click(self.search_icon_path)
        return self.get_text(self.search_page_title_path).strip()

    def Notification_fun(self):
        self.move_element(self.notification_path)
        return self.get_text(self.open_notification).strip()

    def click_show_all_notification(self):
        self.move_element(self.notification_path)
        original_window = self.driver.current_window_handle
        self.click(self.show_all_notification)
        time.sleep(0.5)
        self.window_handle(original_window,self.text_verify_path)


