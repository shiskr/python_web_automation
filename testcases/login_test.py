from pages.login_page import LoginPage
from utility.drivermanager import DriverManager
from assest.constants import *


class TestFacebookLogin(DriverManager):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.verify_facebook_login_page()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()