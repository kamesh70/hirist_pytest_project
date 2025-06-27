import time

import pytest

from pages.login_page import LoginPage
from config.config_page import EMAIL,PASSWORD

@pytest.mark.usefixtures("driver")
class Test_login:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login =LoginPage(driver)


    def test_sign(self):
        self.login.sign_in_fun()

    def test_driver_login(self):
        self.login.driver_login(EMAIL,PASSWORD) #valid password and email
        time.sleep(100)

