import unittest
import logging
from selenium import webdriver
import sys
from assets.constants import *

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DriverManager(unittest.TestCase):

    def setUp(self):
        logging.info("## SETUP METHOD ##")
        if browser is "chrome":
            logging.info("# Initializing the Chrome webdriver.")

            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            # chrome_options.add_argument("--disable-setuid-sandbox")
            chrome_options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(
                executable_path="/Users/kumar.shishir/PycharmProjects/automationsample/assets/chromedriver",
                chrome_options=chrome_options)

        elif browser is "firefox":
            browser_profile = webdriver.FirefoxProfile()
            browser_profile.set_preference("dom.webnotifications.enabled", False)
            self.driver = webdriver.Firefox(
                executable_path="/Users/kumar.shishir/PycharmProjects/automationsample/assets/geckodriver",
                firefox_profile=browser_profile
            )
        elif browser is "safari":
            logging.info("# Initializing the Safari webdriver.")
            self.driver = webdriver.Safari()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.facebook.com")

    def teardown(self):
        logging.info("## TEARDOWN METHOD ##")
        if sys.exc_info()[0]:
            logging.info("# Taking screenshot.")
            test_method_name = self.testMethodName
            self.driver.save_screenshot("./..screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# Removing the webdriver.")
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
