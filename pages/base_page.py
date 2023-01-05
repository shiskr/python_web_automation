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
