import unittest
from src.zipcode_information import ZipCodeInformation
import unittest.mock


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

    def test_zipcode_city_for_houston_zipcode_service_working(self):
        self.zipcodeInfo.set_zipcode("77004")
        self.assertEqual("Houston", self.zipcodeInfo.get_city())

    def test_zipcode_state_for_los_angeles_zipcode_service_working(self):
        self.zipcodeInfo.set_zipcode("90044")
        self.assertEqual("Los Angeles", self.zipcodeInfo.get_city())

    def test_zipcode_state_for_texas_service_working(self):
        self.zipcodeInfo.set_zipcode("77070")
        self.assertEqual("TX", self.zipcodeInfo.get_state())

    def test_zipcode_state_for_new_york_service_working(self):
        self.zipcodeInfo.set_zipcode("10001")
        self.assertEqual("NY", self.zipcodeInfo.get_state())







