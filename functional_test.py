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

		# add underwriters

		underwriter_link = self.browser.find_element_by_link_text('Underwriters')
		underwriter_link.click()

		add_underwriter_link = self.browser.find_element_by_link_text('Add underwriter')
		add_underwriter_link.click()

		underwriter_name = self.browser.find_element_by_name('underwriter_name')
		underwriter_name.send_keys('Manulife')

		underwriter_name = self.browser.find_element_by_name('underwriter_email')
		underwriter_name.send_keys('manulife@manulife.co.uk')

		office_address = self.browser.find_element_by_name('head_office_address')
		office_address.send_keys('Emerald Avenue, Ortigas Center, Pasig City')

		contact_number = self.browser.find_element_by_name('underwriter_contact_number')
		contact_number.send_keys('09988877787')

		contact_person = self.browser.find_element_by_name('contact_person')
		contact_person.send_keys('Richard Yap')

		username = self.browser.find_element_by_name('username')
		username.send_keys('manulife')

		password = self.browser.find_element_by_name('password')
		password.send_keys('manulife')
		password.send_keys(Keys.RETURN)

		home_link = self.browser.find_element_by_link_text('Home')
		home_link.click()


		# add users

		users_link = self.browser.find_element_by_link_text('Users')
		users_link.click()

		add_user_link = self.browser.find_element_by_link_text('Add user')
		add_user_link.click()

		username = self.browser.find_element_by_name('username')
		username.send_keys('user1')

		password = self.browser.find_element_by_name('password1')
		password.send_keys('user1')

		password_confirm = self.browser.find_element_by_name('password2')
		password_confirm.send_keys('user1')
		password_confirm.send_keys(Keys.RETURN)

		home_link = self.browser.find_element_by_link_text('Home')
		home_link.click()


		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')
