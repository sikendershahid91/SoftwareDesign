import unittest
from src.zipcode_information import ZipCodeInformation

class ZipCodeInformationTest(unittest.TestCase):
	def test_canary(self):
		self.assertTrue(True)

	def setUp(self):
		self.zipcodeInfo = ZipCodeInformation()

	def test_set_zipcode_string(self):
		self.zipcodeInfo.set_zipcode("77004")
		self.assertEqual("77004", self.zipcodeInfo.zipcode)

	def test_set_zipcode_less_than_5_characters_not_accepted(self):
		self.zipcodeInfo.set_zipcode("7777")
		self.assertEqual("", self.zipcodeInfo.zipcode)

	def test_set_zipcode_not_all_numbers_not_accepted(self):
		self.zipcodeInfo.set_zipcode("7777a")
		self.assertEqual("", self.zipcodeInfo.zipcode)



