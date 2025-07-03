import time
import pytest
from pages.detail_page import DetailPage

@pytest.mark.usefixtures("logged_in_driver")
class TestDetails:

    @pytest.fixture(autouse=True)
    def setup_detail_page(self, logged_in_driver):
        self.detail = DetailPage(logged_in_driver)
        self.detail.wait_for_page_load()

    @pytest.mark.parametrize("text",["Search for Jobs, Companies, Courses"])
    def test_detail_flow(self,text):
        assert text == self.detail.search_fun()

    @pytest.mark.parametrize("text",["Notifications"])
    def test_notification(self,text):
       assert text == self.detail.Notification_fun()

    def test_show_all_notification(self):
        self.detail.click_show_all_notification()

    def test_click_on_image(self):
        self.detail.click_on_image_fun()

    def test_list_check_box(self):
        self.detail.list_check_box()

    @pytest.mark.parametrize("backend,name", [
        ("Backend Development", "Java"),
        ("Backend Development", "R"),
        ("Backend Development", "Django"),
        ("Frontend Development", "ReactJS"),
        ("Frontend Development", "UI"),
        ("Frontend Development", "UX"),

    ])
    def test_list_of_backend_development(self,backend,name):
        value=self.detail.list_of_backend_development(backend=backend,name=name)
        print(value)

    @pytest.mark.parametrize("text",["Application Testing","Selenium","kamesh"])   #   in param "kamesh" text is not present in Qulity testing  so this testcase fail
    def test_testing_type(self,text):
        self.detail.select_testing_type(text)

    @pytest.mark.parametrize("text,url", [
        ("Backend Development", "https://www.hirist.tech/c/backend-development-jobs?ref=topnavigation"),
        ("Frontend Development", "https://www.hirist.tech/c/frontend-development-jobs?ref=topnavigation"),
        ("Full Stack", "https://www.hirist.tech/c/full-stack-jobs?ref=topnavigation"),
        ("Mobile Applications", "https://www.hirist.tech/c/mobile-applications-jobs?ref=topnavigation"),
        ("Platform Engineering / SAP/Oracle","https://www.hirist.tech/c/platform-engineering-sap-oracle-jobs?ref=topnavigation"),
        ("Quality Assurance", "https://www.hirist.tech/c/quality-assurance-jobs?ref=topnavigation"),
        ("CyberSecurity", "https://www.hirist.tech/c/cybersecurity-jobs?ref=topnavigation"),
        ("DevOps / SRE", "https://www.hirist.tech/c/devops-sre-jobs?ref=topnavigation"),
        ("Emerging Technologies", "https://www.hirist.tech/c/emerging-technologies-jobs?ref=topnavigation"),
    ])
    def test_list_of_data_in_software_development(self,text,url):
        value=self.detail.list_of_software_development(text)
        assert value == url
