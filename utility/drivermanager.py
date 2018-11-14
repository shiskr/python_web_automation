import unittest
import logging

from selenium import webdriver
import sys
from assest.constants import *

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DriverManager(unittest.TestCase):

	def setUp(self):
		logging.info("## SETUP METHOD ##")
		if browser is "chrome":
			logging.info("# Initializing the Chrome webdriver.")
			self.driver = webdriver.Chrome(executable_path="/Users/kumar.shishir/Documents/PWAF/drivers/chromedriver")
		elif browser is "firefox":
			logging.info("# Initializing the Firefox webdriver.")
			self.driver = webdriver.Firefox(executable_path="/Users/kumar.shishir/Documents/PWAF/drivers/geckodriver")
		elif browser is "safari":
			logging.info("# Initializing the Safari webdriver.")
			self.driver = webdriver.Safari(executable_path="/Users/kumar.shishir/Documents/PWAF/drivers/chromedriver")
		# self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		self.driver.get("https://www.facebook.com")

	def teardown(self):
		logging.info("## TEARDOWN METHOD ##")
		if sys.exc_info()[0]:
			logging.info("# Taking screenshot.")
			test_method_name = self.testMethodName
			self.driver.save_screenshot("./..screenshots/%s.png"%test_method_name)

		if self.driver is not None:
			logging.info("# Removing the webdriver.")
			self.driver.quit()


if __name__ == '__main__':
	unittest.main()
