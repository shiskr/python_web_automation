import logging
from utility.drivermanager import DriverManager
from assets.constants import *


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class Test2ndclass(DriverManager):

    def test_case1(self):
        print("1 : 2nd class Test Case")

    def test_case2(self):
        print("2 : 2nd Test Case")
