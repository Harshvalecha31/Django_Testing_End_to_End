from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
# Create your tests here.


Creating a simple testcase in django
class FirstTest(SimpleTestCase):

	# checking valid value
	def test_valid_value(self):
		self.assertContains(self.client.get(''),"Hello World")

	# Checking invalid value 
	def test_invalid_value(self):
		self.assertNotContains(self.client.get(''),"hello world")


# Creating Live server test cases for static files
class FormTest(StaticLiveServerTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.selenium = webdriver.Chrome("D:\Selenium_Essentials\chromedriver.exe")
		cls.selenium.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super().tearDownClass()

	# Hardcoded value for test case 
	def test_form(self):
		self.selenium.get('{}'.format(self.live_server_url))
		name = self.selenium.find_element_by_id("id_name")
		name.send_keys("hammer")
		age = self.selenium.find_element_by_id("id_age")
		age.send_keys(13)
		standard = self.selenium.find_element_by_id("id_standard")
		standard.send_keys(14)
		self.selenium.find_element_by_id("btn1").click()

		# getting all the rows and checking for name
		details = self.selenium.find_elements_by_xpath("//td")
		for i in details:
			if i.text=="hammer":
				print("Yes Present")




