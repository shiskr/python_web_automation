class CommonHelper():

	def navigateToUrl(self, url):
		try:
			self.driver.get(url)
		except:
			#signal something was wrong, or handle the exception appropriately here according to your needs
			raise

	def navigateToUrl(self, url):
		try:
			self.driver.get(url)
		except:
			#signal something was wrong, or handle the exception appropriately here according to your needs
			raise

	def search(self, searchString):
		try:
			#find search field in webpage using XPATH
			input = self.driver.find_elements_by_xpath('//input[@type="text" and @name="q"]')[0]
			#check if input is accessible to the user
			if not input.is_displayed():
				raise Exception("Search field not found.")
			#clear contents of search field
			input.clear()
			#type in query followed by the ENTER key to trigger the search
			input.send_keys(searchString + Keys.RETURN)
		except:
			#signal something was wrong, or handle the exception appropriately here according to your needs
			raise

	def waitForPageTitle(self, expectedTitle, timeout = 30):
		while timeout > 0:
			timeout = timeout - 1
			time.sleep(1)
			if expectedTitle in self.driver.title:
				break
		if timeout <= 0 and (expectedTitle not in self.driver.title):
			return False
		return True