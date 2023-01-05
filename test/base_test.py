import logging
from utility.drivermanager import DriverManager
from assets.constants import *

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class BaseTest(DriverManager):
    def __init__(self):
        pass