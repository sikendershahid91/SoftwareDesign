import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import _patch_dict
from src.weather_report import WeatherReport, ZipcodeInformation


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()
        self.weatherReport.read_list = MagicMock(name='read_list')
        self.zipcodeInformation = ZipcodeInformation()
        self.zipcodeInformation.get_zipcode_location = MagicMock(name='get_zipcode_location')
        self.zipcodeInformation.get_zipcode_location.return_value = {'city': 'changed_city', 'state': 'changed_state'}

    def test_dictionary_set_up_when_read_zipcode_with_exception_if_invalid_zipcode_type(self):
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["123456"])
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["123$a"])
        self.weatherReport.add_zipcode(['77498'])
        self.assertEqual({'77498': {'city': 'empty_data', 'state': 'empty_data'}},
                         self.weatherReport.zipcode_dictionary)

    def test_read_zipcode_return_correct_data_and_format(self):
        zipcode_list = self.weatherReport.read_list.return_value = ["77498"]
        self.weatherReport.add_zipcode(zipcode_list)
        zipcode_data = self.zipcodeInformation.get_zipcode_location
        with _patch_dict(self.weatherReport.zipcode_dictionary["77498"], zipcode_data):
            assert self.weatherReport.zipcode_dictionary["77498"] == zipcode_data
            print(self.weatherReport.zipcode_dictionary)

    def test_read_3_zipcode_return_correct_data_and_format_(self):
        zipcode_list = self.weatherReport.read_list.return_value = ["77498", "77074", "77450"]
        self.weatherReport.add_zipcode(zipcode_list)
        print(zipcode_list)
        pass

        # def test_read_empty_list_return_empty_dictionary(self):
        #     zipcode_list = self.weatherReport.read_list.return_value = [" "]
        #     self.weatherReport.add_zipcode(zipcode_list)
        #     pass
