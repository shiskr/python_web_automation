from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage_OR(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.facebook_title_button = (By.XPATH, "//a[@class='_19eb']")
        self.lefts_ide_nodes = (By.XPATH, "//div[@id='left_nav_section_nodes']")
        self.facebook_status_box = (By.XPATH, "//textarea[@id=\'js_dd\']")
        self.navigation_menu = (By.XPATH, "//div[@id='userNavigationLabel']")
        self.logout_button = (By.XPATH, "//span[text()='Log Out']")
