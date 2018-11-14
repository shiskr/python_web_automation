import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DriverFuncLib:

	def __init__(self,driver):
		self.driver = driver

	def wait_for_element(self, locator, timeout=20):
		logging.info("# Wait for element to appear... %s" % locator)
		WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(By.XPATH, locator))

	def assert_and_click(self, locator):
		self.wait_for_element(*locator)
		logging.info("# Click on element %s" % locator)
		ele = self.driver.find_element(*locator)
		ele.click()

	def is_element_present(self, locator):
		try:
			self.driver.find_element(*locator)
			logging.info("# Element '%s' is present." % locator)
			return True
		except NoSuchElementException:
			logging.info("# Element '%s' is not present." % locator)
			return False

	def assert_element_present(self, locator):
		logging.info("# Verifying Element is present.")
		assert self.is_element_present(locator), "Element '%s' should be present." % locator

	def assert_element_is_not_present(self, locator):
		logging.info("# Verifying Element is not present.")
		assert not self.is_element_present(locator), "Element '%s' should not be present." % locator

	def wait_for_element_visible(self, locator, timeout=20):
		logging.info("# Wait for element to appear... %s" % locator)
		WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))

	def wait_for_element_invisible(self, locator, timeout=20):
		logging.info("# Wait for element to appear... %s" % locator)
		WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))

	def is_element_visible(self, locator):
		try:
			ele = self.driver.find_element(*locator)
			return ele.is_displayed()
		except NoSuchElementException:
			logging.info("# Element '%s' is not present." % locator)
		return False

	def assert_element_visibility(self, locator, is_visible=True):
		logging.info("# Verifying Element visibility.")
		assert is_visible == self.is_element_visible(locator), "Element '%s' visibility should be %s." % (locator, is_visible)

	def enter_text_textbox(self, locator, text):
		ele = self.driver.find_element(*locator)
		try:
			logging.info("# Entering text in Textbox.")
			ele.clear()
			ele.send_keys(text)
			return True
		except NoSuchElementException:
			return False
