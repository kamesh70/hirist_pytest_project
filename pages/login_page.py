from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.hirist_home_page import HiristHomePage

class LoginPage(HiristHomePage):  # Already inherits all BasePage methods

    sign_in_path = (By.XPATH, "//a[text()='Sign In']")
    email_path =(By.XPATH,"//input[@name='email']")
    password_path =(By.XPATH,"//input[@name='password']")
    login_path=(By.XPATH,"//button[@type='submit' and text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)  # pass driver to parent classes

    def sign_in_fun(self):
        self.click_jobseeker_button()       # inherited method from HiristHomePage
        self.click(self.sign_in_path)       # defined in this class

    def email_fun(self,email):
        self.enter_text(self.email_path,email)

    def password_fun(self,password):
        self.enter_text(self.password_path,password)

    def login_button_fun(self):
        self.click(self.login_path)


    def driver_login(self,email,password):
        self.sign_in_fun()
        self.email_fun(email)
        self.password_fun(password)
        self.login_button_fun()