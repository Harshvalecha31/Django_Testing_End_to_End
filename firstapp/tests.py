from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.


# Creating a simple testcase in django
class FirstTest(SimpleTestCase):

	# checking valid value
	def test_valid_value(self):
		self.assertContains(self.client.get(''),"Hello World")

	# Checking invalid value 
	def test_invalid_value(self):
		self.assertNotContains(self.client.get(''),"hello world")

