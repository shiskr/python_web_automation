import logging
from utility.driver_func_lib import DriverFuncLib
from pages_or.home_page_or import HomePage_OR
from pages.login_page import LoginPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class HomePage(HomePage_OR):

    def __init__(self, driver):
        HomePage_OR.__init__(self, driver)
        self.driver = driver
        self.driver_func_lib = DriverFuncLib(self.driver)

    def click_navigation_menu(self):
        logging.info('## Clicking on Navigation Menu Button ##')
        self.driver_func_lib.assert_and_click(self.navigation_menu)

    def click_logout_button(self):
        logging.info('## Clicking on Logout Button ##')
        self.driver_func_lib.assert_and_click(self.logout_button)
        return LoginPage(self.driver)
