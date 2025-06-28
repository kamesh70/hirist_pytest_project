import time

import pytest
from conftest import logged_in_driver
from pages.search_page import SearchPage

@pytest.mark.usefixtures("logged_in_driver")
class TestSearch:

    @pytest.fixture(autouse=True)
    def setup(self,logged_in_driver):
        self.search =SearchPage(logged_in_driver)

    @pytest.mark.parametrize("text,output", [("Pytest Slenium Manual Testing Api Testing Sdet", "Search For - Pytest Slenium Manual Testing Api Testing Sdet Jobs")])
    def test_search_query(self,text,output):
        assert output == self.search.query_search_fun(text)

    @pytest.mark.parametrize("text",["Pytest Slenium Manual Testing Api Testing Sdet"])
    def test_check_box(self,text):
        self.search.check_box_click(text)
        time.sleep(5)
