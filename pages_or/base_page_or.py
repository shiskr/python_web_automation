from utility.driver_func_lib import DriverFuncLib


class BasePage_OR():

    def __init__(self, driver):
        self.driver = driver
        self.driver_func_lib = DriverFuncLib(self.driver)