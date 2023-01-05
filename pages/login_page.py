import logging
from pages_or.login_page_or import LoginPage_OR
from utility.driver_func_lib import DriverFuncLib
import pages.home_page # do not use 'from' when importing pages

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage(LoginPage_OR):
	def __init__(self, driver):
		LoginPage_OR.__init__(self, driver)
		self.driver = driver
		self.driver_func_lib = DriverFuncLib(self.driver)

	def click_login(self):
		logging.info('## Clicking on Login Button ##')
		self.driver_func_lib.assert_and_click(self.login_button)
		return pages.home_page.HomePage(self.driver)

	def enter_email(self, text):
		logging.info('## Entering Email Address ##')
		self.driver_func_lib.enter_text_textbox(self.email_field, text)

	def enter_password(self, text):
		logging.info('## Entering Password ##')
		self.driver_func_lib.enter_text_textbox(self.password_field, text)
