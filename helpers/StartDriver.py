from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

class startDriver():
   
   def initializeWebdriver(self, driverType, implicitWait=10):
      #initialize appropriate driver, remember to download driver and add it to you PATH environment variable

      if driverType == 'Firefox':
         driver_location = "/Users/kumar.shishir/PycharmProjects/automationsample/assest/geckodriver"
         options = webdriver.FirefoxOptions()
         options.add_argument('--lang=es')
         self.driver = webdriver.Firefox(executable_path=driver_location, firefox_options=options)

      elif driverType == 'Chrome':
         driver_location = "/Users/kumar.shishir/PycharmProjects/automationsample/assest/chromedriver"
         options = webdriver.ChromeOptions()
         options.add_argument('--lang=es')
         self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

      elif driverType == 'Safari':
         self.driver = webdriver.Safari()

      else:
         raise Exception('Unknown webdriver type')
         #for every action do a retry with a 10 seconds timeout by default or user specified
         self.driver.implicitly_wait(implicitWait)
   		 
   def closeBrowser(self):
      try:
         self.driver.close()
      except:
         #signal something was wrong, or handle the exception appropriately here according to your needs
         raise