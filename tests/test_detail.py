import time

import pytest
from pages.detail_page import DetailPage

@pytest.mark.usefixtures("logged_in_driver")
class TestDetails:

    @pytest.fixture(autouse=True)
    def setup_detail_page(self, logged_in_driver):
        self.detail = DetailPage(logged_in_driver)

    @pytest.mark.parametrize("text",["Search for Jobs, Companies, Courses"])
    def test_detail_flow(self,text):
        assert text == self.detail.search_fun()
