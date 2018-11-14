import logging
from pages_or.base_page_or import BasePage_OR
from selenium.webdriver.common.by import By

class BasePage(BasePage_OR):
    def __init__(self, driver):
        self.driver = driver
