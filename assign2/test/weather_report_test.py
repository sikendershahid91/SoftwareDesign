import unittest
from unittest.mock import patch, Mock
from src.weather_report import WeatherReport
from src.zipcode_service import ZipcodeService


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()
        self.zipcodeService = ZipcodeService()

    @patch.object(ZipcodeService, 'get_zipcode_location')
    def test_read_one_zipcode_location_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004']
        mock_zipcode_info.get_zipcode_location.return_value = ('Houston', 'TX')
        self.weatherReport.set_service(mock_zipcode_info)
        self.assertEqual({'77004': ('Houston', 'TX')}, 
            self.weatherReport.read_zipcodes(zipcode_list_to_read))

    @patch.object(ZipcodeService, 'get_zipcode_location')
    def test_read_three_zipcode_location_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_zipcode_info.get_zipcode_location.side_effect = [
            ('Houston', 'TX'),
            ("Beverly Hills", 'CA'),
            ('New York', 'NY')]
        self.weatherReport.set_service(mock_zipcode_info)
        self.assertEqual(
            {'77004': ('Houston', 'TX'),
             '90210': ("Beverly Hills", 'CA'),
             '10001': ('New York', 'NY')},
            self.weatherReport.read_zipcodes(zipcode_list_to_read))

    def test_read_0_zipcode_then_service_not_called(self):
        zipcode_list_to_read = []
        self.assertEqual({}, 
            self.weatherReport.read_zipcodes(zipcode_list_to_read))

    def test_get_invalid_from_service_for_wrong_zipcode_digit(self):
        self.assertEqual('INVALID', 
            self.zipcodeService.get_zipcode_location('a2342'))

    def test_get_invalid_from_service_for_wrong_zipcode_length(self):
        self.assertEqual('INVALID', 
            self.zipcodeService.get_zipcode_location('122342'))

    def test_read_invalid_zipcode(self):
        zipcode_list_to_read = ['a7700']
        self.weatherReport.set_service(self.zipcodeService)
        self.assertEqual({'a7700': 'INVALID'}, 
            self.weatherReport.read_zipcodes(zipcode_list_to_read))


    @patch.object(ZipcodeService, 'get_zipcode_weather')
    def test_read_one_zipcode_weather_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004']
        mock_zipcode_info.get_zipcode_weather.return_value = (
            ('20', '25', 'sunny'))
        self.weatherReport.set_service(mock_zipcode_info)
        self.assertEqual({'77004': ('20', '25', 'sunny')}, 
            self.weatherReport.read_weather(zipcode_list_to_read))

    @patch.object(ZipcodeService, 'get_zipcode_weather')
    def test_read_three_zipcode_weather_when_service_working(
            self, mock_zipcode_info):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_zipcode_info.get_zipcode_weather.side_effect = [
            ('20', '25', 'sunny'),
            ('45', '70', 'mostly cloudy'),
            ('65', '44', 'rainy day')]
        self.weatherReport.set_service(mock_zipcode_info)
        self.assertEqual(
            {'77004': ('20', '25', 'sunny'),
             '90210': ('45', '70', 'mostly cloudy'),
             '10001': ('65', '44', 'rainy day')},
            self.weatherReport.read_weather(zipcode_list_to_read))

    def test_read_0_weather_then_service_not_called(self):
        zipcode_list_to_read = []
        self.assertEqual({}, 
            self.weatherReport.read_weather(zipcode_list_to_read))


