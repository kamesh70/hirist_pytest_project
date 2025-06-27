import pytest

from pages.hirist_home_page import HiristHomePage


@pytest.mark.usefixtures("driver")
class TestHirist:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.hirist = HiristHomePage(driver)

    def test_jobseeker_button(self):
        self.hirist.click_jobseeker_button()