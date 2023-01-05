from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage_OR(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
