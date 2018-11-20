from selenium.webdriver.common.alert import Alert
import logging
from pages.login_page import LoginPage
from utility.drivermanager import DriverManager
from assets.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class TestFacebookLogin(DriverManager):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.verify_facebook_login_page()
        login_page.enter_email(email)
        login_page.enter_password(password)
        home_page = login_page.click_login()
        # try:
        #     Alert(self.driver).accept()
        #     # Alert(driver).dismiss()
        #
        # except:
        #     print("no alert")
        home_page.click_navigation_menu()
        login_page = home_page.click_logout_button()
