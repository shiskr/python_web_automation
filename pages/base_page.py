import logging
from pages_or.base_page_or import BasePage_OR
from utility.driver_func_lib import DriverFuncLib

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class BasePage(BasePage_OR):
    def __init__(self, driver):
        BasePage_OR.__init__(self, driver)
        self.driver = driver
        self.driver_func_lib = DriverFuncLib(self.driver)

    # def click_logout(self):
    #     logging.info('## Clicking on Logout Button ##')
    #     self.driver_func_lib.assert_and_click(self.navigation_menu)
    #     self.driver_func_lib.assert_and_click(self.logout_button)
    #     login_page = LoginPage(self.driver)
    #     return login_page
