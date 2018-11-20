import logging
from pages_or.login_page_or import LoginPage_OR
from utility.driver_func_lib import DriverFuncLib

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage(LoginPage_OR):
	def __init__(self, driver):
		LoginPage_OR.__init__(self, driver)
		self.driver = driver
		self.driver_func_lib = DriverFuncLib(self.driver)
		self.title = "Facebook"
		# self.xpath_link = ""
		# self.facebookStatusBox = (By.XPATH, "//textarea[@id=\'js_dd\']")
		# self.facebookTitleBtn = "//a[@class='_19eb']"
		# self.leftSideNodes = "//div[@id='left_nav_section_nodes']"
		#
		# self.email_field = "//input[@id='email']"
		# self.password_field = "//input[@id='pass']"
		# self.login_button = "//label[@id='loginbutton']"

	def verify_facebook_login_page(self):
		logging.info('## Verifying home page ##')
		actual_title = self.driver.title
		logging.info('# Actual Title: %s' % actual_title)
		assert self.title in actual_title, "Actual title %s, should be same as %s" % (actual_title, self.title)
		# print('True')
		return self

	def click_login(self):
		logging.info('## Clicking on Login Button ##')
		self.driver_func_lib.assert_and_click(self.login_button)
		# return HomePage(self.driver)
		return HomePage(self.driver)

	def enter_email(self, text):
		logging.info('## Entering Email Address ##')
		self.driver_func_lib.enter_text_textbox(self.email_field, text)

	def enter_password(self, text):
		logging.info('## Entering Password ##')
		self.driver_func_lib.enter_text_textbox(self.password_field, text)


from pages.home_page import HomePage
