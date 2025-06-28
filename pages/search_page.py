import time
from selenium.webdriver.common.by import By
from pages.detail_page import DetailPage

class SearchPage(DetailPage):

    input_search_path=(By.XPATH,"//input[@name='query']")
    search_button_path=(By.XPATH,"//button[text()='Search']")
    assert_h1 =(By.XPATH,"//h1[contains(@class,'mui-style-1cayejn')]")
    check_box_path=(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-j3syvn']")
    selected_check_box =(By.XPATH,"//p[contains(@class,'mui-style-1gqd86t')]")
    apply_button=(By.XPATH,"//button[text()='Apply All']")
    thanks_path=(By.XPATH,"//p[contains(@class,'mui-style-ao4w7g')]")


    def __init__(self, driver):
        super().__init__(driver)

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

        search_page_header=self.search_fun()
        assert search_page_header == "Search for Jobs, Companies, Courses"
        self.enter_text(self.input_search_path,text)
        self.click(self.search_button_path)
        value = self.get_text(self.assert_h1).strip()
        print(value)
        return value

    def check_box_click(self,text):
        try:
            self.query_search_fun(text)
            max_scroll=self.scroll_to_bottom()
            print(f"max_scroll elements {max_scroll}")
            original_window = self.driver.current_window_handle
            elements =self.find_elements(self.check_box_path)
            length=len(elements)
            if length == 0:
                print(f"enable check box is not present {length}")
                return
            else:
                print(f"length of total {length}")
                for index,ele in enumerate(elements):
                    print(f"current index {index}")
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", ele)
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ele)
                    time.sleep(0.3)
                    self.actions.move_to_element(ele).click().perform()
                    time.sleep(0.4)
                    if int(index) == 10 :
                        print("brak loop")
                        break
                if length > 1:
                    selected = self.get_text(self.selected_check_box).strip()
                    self.click(self.apply_button)
                    print(selected)
                    time.sleep(1) # time sleep use for capture new window open
                    self.window_handle(original_window,self.thanks_path)
        except Exception as e:
            print(f"Error message:  {e}" )




