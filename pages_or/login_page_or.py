from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage_OR(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.facebookStatusBox = (By.XPATH, "//textarea[@id=\'js_dd\']")
        self.facebookTitleBtn = (By.XPATH, "//a[@class='_19eb']")
        self.leftSideNodes = (By.XPATH, "//div[@id='left_nav_section_nodes']")

        self.email_field = (By.XPATH, "//input[@id='email']")
        self.password_field = (By.XPATH, "//input[@id='pass']")
        # self.login_button = "//label[@id='loginbutton']"
