import unittest
from unittest.mock import patch, Mock
from src.weather_report import WeatherReport
from src.location_service import LocationService
from src.weather_service import WeatherService


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()
        self.locationService = LocationService()

    @patch.object(LocationService, 'get_zipcode_location')
    def test_read_one_zipcode_location_when_service_working(
            self, mock_location):
        zipcode_list_to_read = ['77004']
        mock_location.get_zipcode_location.return_value = ('Houston', 'TX')
        self.weatherReport.set_location_service(mock_location)
        self.assertEqual({'77004': ('Houston', 'TX')},
                         self.weatherReport.get_cities_and_state(zipcode_list_to_read))

    @patch.object(LocationService, 'get_zipcode_location')
    def test_read_three_zipcode_location_when_service_working(
            self, mock_location):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_location.get_zipcode_location.side_effect = [
            ('Houston', 'TX'),
            ("Beverly Hills", 'CA'),
            ('New York', 'NY')]
        self.weatherReport.set_location_service(mock_location)
        self.assertEqual(
            {'77004': ('Houston', 'TX'),
             '90210': ("Beverly Hills", 'CA'),
             '10001': ('New York', 'NY')},
            self.weatherReport.get_cities_and_state(zipcode_list_to_read))

    def test_read_0_zipcode_then_service_not_called(self):
        zipcode_list_to_read = []
        self.assertEqual({},
                         self.weatherReport.get_cities_and_state(zipcode_list_to_read))

    def test_get_cities_and_state_with_invalid_zipcode(self):
        zipcode_list_to_read = ['a7700']
        self.weatherReport.set_location_service(self.locationService)
        self.assertEqual({'a7700': 'INVALID'},
                         self.weatherReport.get_cities_and_state(zipcode_list_to_read))

    @patch.object(WeatherService, 'get_zipcode_weather')
    def test_read_one_zipcode_weather_when_service_working(
            self, mock_weather):
        zipcode_list_to_read = ['77004']
        mock_weather.get_zipcode_weather.return_value = (
            ('20', '25', 'sunny'))
        self.weatherReport.set_weather_service(mock_weather)
        self.assertEqual({'77004': ('20', '25', 'sunny')},
                         self.weatherReport.get_weather_data(zipcode_list_to_read))

    @patch.object(WeatherService, 'get_zipcode_weather')
    def test_read_three_zipcode_weather_when_service_working(
            self, mock_weather):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_weather.get_zipcode_weather.side_effect = [
            ('20', '25', 'sunny'),
            ('45', '70', 'mostly cloudy'),
            ('65', '44', 'rainy day')]
        self.weatherReport.set_weather_service(mock_weather)
        self.assertEqual(
            {'77004': ('20', '25', 'sunny'),
             '90210': ('45', '70', 'mostly cloudy'),
             '10001': ('65', '44', 'rainy day')},
            self.weatherReport.get_weather_data(zipcode_list_to_read))

    def test_read_0_weather_then_service_not_called(self):
        zipcode_list_to_read = []
        self.assertEqual({},
                         self.weatherReport.get_weather_data(zipcode_list_to_read))

    @patch.object(WeatherService, 'get_zipcode_weather')
    def test_coldest_zipcode_weather_from_3_cities(
            self, mock_weather):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_weather.get_zipcode_weather.side_effect = [
            ('20', '25', 'sunny'),
            ('45', '70', 'mostly cloudy'),
            ('65', '44', 'rainy day')]
        self.weatherReport.set_weather_service(mock_weather)
        self.assertEqual(
            '77004',
            self.weatherReport.get_coldest_city(zipcode_list_to_read))

    @patch.object(WeatherService, 'get_zipcode_weather')
    def test_hottest_zipcode_weather_from_3_cities(
            self, mock_weather):
        zipcode_list_to_read = ['77004', '90210', '10001']
        mock_weather.get_zipcode_weather.side_effect = [
            ('20', '25', 'sunny'),
            ('45', '70', 'mostly cloudy'),
            ('65', '44', 'rainy day')]
        self.weatherReport.set_weather_service(mock_weather)
        print(self.weatherReport.get_hottest_city(zipcode_list_to_read))
        # self.assertEqual(
        #     '90210',
        #     self.weatherReport.get_hottest_city(zipcode_list_to_read))
