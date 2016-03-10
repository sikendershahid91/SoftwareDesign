import unittest
from unittest.mock import patch, Mock
from src.weather_service import WeatherService


class WeatherServiceTest(unittest.TestCase):
    def setUp(self):
        self.weatherService = WeatherService()

    def test_get_invalid_from_service_for_wrong_zipcode_digit(self):
        self.assertEqual('INVALID',
                         self.weatherService.get_zipcode_weather('a2342'))

    def test_get_invalid_from_service_for_wrong_zipcode_length(self):
        self.assertEqual('INVALID',
                         self.weatherService.get_zipcode_weather('122342'))

    @patch('src.weather_service.requests.get')
    def test_not_successful_http_connection_output(self, mock_get):
        mock_response = Mock(status_code=404)
        mock_get.return_value = mock_response
        self.assertEqual('ERROR',
                         self.weatherService.get_zipcode_weather('77004'))

    @patch('src.location_service.requests.get')
    def test_get_correct_location_from_successful_json_data(self, mock_get):
        mock_response = Mock(status_code=200)
        with open('test/weather_service_successful_response.xml', 'r') as f:
            mock_response.content = f.read()
        mock_get.return_value = mock_response
        self.assertEqual(('41', '48', 'Rain'),
                         self.weatherService.get_zipcode_weather('77004'))
