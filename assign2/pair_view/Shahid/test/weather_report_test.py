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

    def test_dictionary_set_up_when_read_zipcode_with_exception_if_invalid_zipcode_type(self):
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["123456"])
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["123$a"])
        self.weatherReport.add_zipcode(['77498'])
        self.assertEqual({'77498': {'city': 'empty_data', 'state': 'empty_data'}},
                         self.weatherReport.zipcode_dictionary)

    def test_read_zipcode_return_correct_data_and_format(self):
        zipcode_list = self.weatherReport.read_list.return_value = ["77498"]
        self.weatherReport.add_zipcode(zipcode_list)
        zipcode_data = self.zipcodeInformation.get_zipcode_location.return_value = {'city': 'Sugar Land', 'state': 'TX'}
        self.weatherReport.zipcode_dictionary['77498'] = zipcode_data
        self.assertEqual({'city': 'Sugar Land', 'state': 'TX'}, self.weatherReport.zipcode_dictionary['77498'])

    def test_read_3_zipcode_return_correct_data_and_format_(self):
        zipcode_list = self.weatherReport.read_list.return_value = ["77498", "77074", "77450"]
        self.weatherReport.add_zipcode(zipcode_list)
        _77498_data = self.zipcodeInformation.get_zipcode_location.return_value = {'city': 'Sugar Land', 'state': 'TX'}
        _77074_data = self.zipcodeInformation.get_zipcode_location.return_value = {'city': 'Houston', 'state': 'TX'}
        _77450_data = self.zipcodeInformation.get_zipcode_location.return_value = {'city': 'Katy', 'state': 'TX'}
        self.weatherReport.set_zipcode('77498', _77498_data)
        self.weatherReport.set_zipcode('77074', _77074_data)
        self.weatherReport.set_zipcode('77450', _77450_data)
        self.assertEqual({'city': 'Sugar Land', 'state': 'TX'}, self.weatherReport.zipcode_dictionary['77498'])
        self.assertEqual({'city': 'Houston', 'state': 'TX'}, self.weatherReport.zipcode_dictionary['77074'])
        self.assertEqual({'city': 'Katy', 'state': 'TX'}, self.weatherReport.zipcode_dictionary['77450'])


        # def test_read_empty_list_return_empty_dictionary(self):
        #     zipcode_list = self.weatherReport.read_list.return_value = [" "]
        #     self.weatherReport.add_zipcode(zipcode_list)
        #     pass
