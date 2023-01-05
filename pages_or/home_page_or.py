from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage_OR(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.logo = (By.CSS_SELECTOR, "img.logo")
        self.header = (By.CSS_SELECTOR, "img.logo + span")
        self.account_link = (By.ID, "navbarAccount")
        self.login_button = (By.ID, "navbarLoginButton")
        self.dismiss_btn = (By.XPATH, "//span[text()='Dismiss']")
