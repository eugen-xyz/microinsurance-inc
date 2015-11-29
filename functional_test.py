from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import unittest

class AdminLogInTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		#self.browser.quit()
		pass

	def test_admin_can_log_in_to_the_site_administration(self):
		self.browser.get('http://localhost:8000/admin')
		self.assertIn('Log in', self.browser.title)

		username = self.browser.find_element_by_name('username')
		username.send_keys('admin')

		password = self.browser.find_element_by_name('password')
		password.send_keys('admin')
		password.send_keys(Keys.RETURN)

		
	# def test_admin_can_add_underwriter_details(self):
		# self.browser.get('http://localhost:8000/admin')
		underwriter_link = self.browser.find_element_by_link_text('Underwriters')
		underwriter_link.click()

		add_underwriter_link = self.browser.find_element_by_link_text('Add underwriter')
		add_underwriter_link.click()

		


		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')
