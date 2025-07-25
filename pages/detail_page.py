import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.dynamic_locators import paragraph_by_text,link_by_a_text,link_by__li_a_text
from utils.locators import DetailsPageLocators

class DetailPage(BasePage):
    search_icon_path = (By.XPATH,"//div[@data-testid='search_icon']")
    verify_search=(By.XPATH,"//p[text()='Search for Jobs, Companies, Courses']")
    search_page_title_path =(By.XPATH,"//p[contains(@class,'mui-style-bzxy8k')]")
    notification_path=(By.XPATH,"//span[contains(@class,'MuiBadge-root mui-style-x0z9yr')]")
    open_notification=(By.XPATH,"//p[contains(@class,'mui-style-9npega')]")
    show_all_notification=(By.XPATH,"//a[contains(@class,'mui-style-1eo38lg')]")
    text_verify_path =(By.XPATH,"//p[contains(@class,'mui-style-15fxu1t')]")
    infinite_scroll_path=(By.CLASS_NAME, "infinite-scroll-component")
    check_box_path=(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-j3syvn']")  # change this to your repeating item selector
    software_dev_path =(By.XPATH,"//button[text()='Software Development']")
    quality_ass_path=(By.XPATH,"//li/a[text()='Quality Assurance']")

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DetailsPageLocators()

    def get_a_tag_text(self,text):
        return link_by_a_text(text)

    def get_li_a_tag_text(self,text):
        return link_by__li_a_text(text)

    def get_p_tag_text(self,text):
        return paragraph_by_text(text)

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

    def click_on_image_fun(self):
        self.click(self.locators.user_image)

    def list_check_box(self):
        try:
            self.scroll_to_bottom()
        except Exception as e:
            print(e)

    def list_of_software_development(self,name):
        self.move_element(self.software_dev_path)
        self.click(self.get_li_a_tag_text(name))
        self.wait_for_page_load()
        return self.current_page_url

    def list_of_backend_development(self,backend,name):
        self.move_element(self.software_dev_path)
        self.move_element(self.locators.dynamic_xpath_using_a_tage(backend))
        self.click(self.locators.dynamic_xpath_using_a_tage(name))
        self.wait_for_page_load()
        return self.current_page_url



    def select_testing_type(self,name):
        self.move_element(self.software_dev_path)
        self.move_element(self.quality_ass_path)
        self.click(self.locators.dynamic_xpath_using_a_tage(name))
        self.wait_for_page_load()
        self.check_box()
        return self.current_page_url

    def edit_profile_fun(self, tab):
        self.click_on_image_fun()
        self.click(self.get_p_tag_text(tab))
        self.wait_for_page_load()
        return self.current_page_url

    def user_image_under_list(self,tag):
        self.click_on_image_fun()
        self.click(self.get_a_tag_text(tag))
        original_window=self.driver.current_window_handle
        return self.window_handle(original_window)
