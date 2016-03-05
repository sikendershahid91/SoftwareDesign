import unittest
from unittest.mock import patch, Mock
from src.weather_report import WeatherReport, ZipcodeServiceInterface


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()

    # def test_read_zipcode_5_digit(self):
    #     self.weatherReport.read_zipcodes(["12345"])
    #     self.assertEqual(['12345'], self.weatherReport.zipcode_location_dictionary.keys())

    @patch.object(ZipcodeServiceInterface, 'get_zipcode_location')
    def test_read_one_zipcode_location_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004']
        mock_zipcode_info.get_zipcode_location.return_value = ('Houston', 'TX')
        self.weatherReport.set_location_service(mock_zipcode_info)
        self.assertEqual({'77004': ('Houston', 'TX')}, self.weatherReport.read_zipcodes(zipcode_list_to_read))

    @patch.object(ZipcodeServiceInterface, 'get_zipcode_location')
    def test_read_three_zipcode_location_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_zipcode_info.get_zipcode_location.side_effect = [
            ('Houston', 'TX'),
            ("Beverly Hills", 'CA'),
            ('New York', 'NY')]
        self.weatherReport.set_location_service(mock_zipcode_info)
        self.assertEqual(
            {'77004': ('Houston', 'TX'),
             '90210': ("Beverly Hills", 'CA'),
             '10001': ('New York', 'NY')},
            self.weatherReport.read_zipcodes(zipcode_list_to_read))

    def test_read_0_zipcode_service_not_called(self):
        zipcode_list_to_read = []
        self.assertEqual({}, self.weatherReport.read_zipcodes(zipcode_list_to_read))

    @patch.object(ZipcodeServiceInterface, 'get_zipcode_weather')
    def test_read_one_zipcode_location_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004']
        mock_zipcode_info.get_zipcode_weather.return_value = ('Houston', 'TX')
        self.weatherReport.set_location_service(mock_zipcode_info)
        self.assertEqual({'77004': ('Houston', 'TX')}, self.weatherReport.read_zipcodes(zipcode_list_to_read))

    @patch.object(ZipcodeServiceInterface, 'get_zipcode_weather')
    def test_read_three_zipcode_location_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_zipcode_info.get_zipcode_weather.side_effect = [
            ('20', '25', 'sunny'),
            ('45', '70', 'mostly cloudy'),
            ('65', '44', 'rainy day')]
        self.weatherReport.set_location_service(mock_zipcode_info)
        self.assertEqual(
            {'77004': ('20', '25', 'sunny'),
             '90210': ('45', '70', 'mostly cloudy'),
             '10001': ('65', '44', 'rainy day')},
            self.weatherReport.read_zipcodes(zipcode_list_to_read))