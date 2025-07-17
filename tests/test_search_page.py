import time
import pytest,os
from conftest import logged_in_driver
from pages.search_page import SearchPage
from utils.data_loader import load_excel_data


# path to Excel file
base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(base_dir, "../config/search_data.xlsx")

@pytest.mark.usefixtures("logged_in_driver")
class TestSearch:
    # search_obj=load_excel_data(excel_path, sheet_name="sea")
    search_obj = load_excel_data(excel_path, sheet_name="sea", columns=["text", "output"])
    search_texts = [(text) for text, _ in search_obj]  # reduce to [(text,), ...]

    @pytest.fixture(autouse=True)
    def setup(self,logged_in_driver):
        self.search =SearchPage(logged_in_driver)

    @pytest.mark.parametrize("text,output", search_obj)
    def test_search_query(self,text,output):
        assert output == self.search.query_search_fun(text)

    @pytest.mark.parametrize("text",search_texts)
    def test_check_box(self,text):
        print(f"data: {text}")
        self.search.check_box_click(text)
        time.sleep(0.8)
