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
    ])
    def test_list_of_backend_development(self,backend,name):
        value=self.detail.list_of_backend_development(backend=backend,name=name)
        print(value)

    @pytest.mark.parametrize("value",["Application Testing","Selenium","Mobile Testing","White Box Testing","Automation Testing Tools",])
    @pytest.mark.smoke
    def test_testing_type(self,value):
        self.detail.select_testing_type(value)

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

    @pytest.mark.parametrize("tab,url", [("EDIT", "https://www.hirist.tech/registration/addPersonalDetails")])
    def test_edit_profile(self,tab,url):
        value=self.detail.edit_profile_fun(tab)
        print("return value ",value)
        assert value == url

    @pytest.mark.parametrize("tab,url",[("My Profile","https://www.hirist.tech/myprofile"),("Settings","https://www.hirist.tech/settings?section=emailnotification"),("Get the hirist app","https://www.hirist.tech/downloadapp?ref=menu"),("Blocked Companies","https://www.hirist.tech/settings?section=privacy"),("Applied Jobs","https://www.hirist.tech/applied-jobs"),("Pending Assessments","https://www.hirist.tech/pendingassessments"),("My Interviews","https://www.hirist.tech/interviews"),("My Jobfeed","https://www.hirist.tech/jobfeed?minexp=2&maxexp=3"),("Change Password","https://www.hirist.tech/settings?section=changepassword"),("Request Recommendation","https://www.hirist.tech/myprofile"),("Learning Center","https://www.hirist.tech/learning?ref=menu"),])
    def test_user_image_under_list_tab(self,tab,url):
        value=self.detail.user_image_under_list(tab)
        assert value ==url

