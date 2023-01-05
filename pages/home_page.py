import logging
import pages.login_page # do not use 'from' when importing pages
from utility.driver_func_lib import DriverFuncLib
from pages_or.home_page_or import HomePage_OR

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class HomePage(HomePage_OR):

    title = "OWASP Juice Shop"

    def __init__(self, driver):
        HomePage_OR.__init__(self, driver)
        self.driver = driver
        self.driver_func_lib = DriverFuncLib(self.driver)

    def verify_welcome_page(self):
        logging.info('## Verifying home page ##')
        actual_title = self.driver.title
        logging.info('# Actual Title: ${0}'.format(actual_title))
        assert self.title in actual_title, "Actual title %s, should be same as %s" % (actual_title, self.title)
        return self

    def click_login_button(self):
        logging.info('## Clicking on Logout Button ##')
        self.driver_func_lib.assert_and_click(self.account_link)
        self.driver_func_lib.assert_and_click(self.login_button)
        return pages.login_page.LoginPage(self.driver)
    
    def click_dismiss_btn(self):
        self.driver_func_lib.assert_and_click(self.dismiss_btn)