from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage_OR(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.email_field = (By.XPATH, "//input[@id='email']")
        self.password_field = (By.XPATH, "//input[@id='pass']")
        self.login_button = (By.XPATH, "//label[@id='loginbutton']")
