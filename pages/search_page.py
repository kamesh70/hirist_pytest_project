import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.detail_page import DetailPage

class SearchPage(BasePage):

    input_search_path=(By.XPATH,"//input[@name='query']")
    search_button_path=(By.XPATH,"//button[text()='Search']")
    assert_h1 =(By.XPATH,"//h1[contains(@class,'mui-style-1cayejn')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.detail = DetailPage(driver)  # Instance of SearchPage


    def scroll_to_bottom(self):
        scrollable_div = self.driver.find_element(By.CSS_SELECTOR, "div.infinite-scroll-component")
        previous_height = 0
        while True:
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(2)  # Wait for content to load
            items = self.driver.find_elements(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-j3syvn']") # change this to your repeating item selector
            current_count = len(items)

            if current_count == previous_height:
                break
            previous_height = current_count
        return current_count

    def query_search_fun(self,text):

        search_page_header=self.detail.search_fun()
        assert search_page_header == "Search for Jobs, Companies, Courses"
        self.enter_text(self.input_search_path,text)
        self.click(self.search_button_path)
        value = self.get_text(self.assert_h1).strip()
        print(value)
        return value

    def check_box_click(self,text):
        try:
            self.query_search_fun(text)
            self.check_box()
        except Exception as e:
            print(f"Error message:  {e}" )




