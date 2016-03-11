import unittest
from unittest.mock import patch, Mock
from src.location_service import LocationService


class LocationServiceTest(unittest.TestCase):
    def setUp(self):
        self.locationService = LocationService()

    def test_get_invalid_from_service_for_wrong_zipcode_digit(self):
        self.assertEqual('INVALID',
                         self.locationService.get_zipcode_location('a2342'))

    def test_get_invalid_from_service_for_wrong_zipcode_length(self):
        self.assertEqual('INVALID',
                         self.locationService.get_zipcode_location('122342'))

    @patch('src.location_service.requests.get')
    def test_not_successful_http_connection_output(self, mock_get):
        mock_response = Mock(status_code=404)
        mock_get.return_value = mock_response
        self.assertEqual('ERROR',
                         self.locationService.get_zipcode_location('77004'))

    @patch('src.location_service.requests.get')
    def test_get_correct_location_from_successful_json_data(self, mock_get):
        mock_response = Mock(status_code=200)
        mock_response.json.return_value = (
            {
                "results": [
                    {
                        "address_components": [
                            {
                                "long_name": "Houston",
                                "types": ["locality", "political"]
                            },
                            {
                                "short_name": "TX",
                                "types": ["administrative_area_level_1", "political"]
                            },
                        ],
                    }
                ],
                "status": "OK",
            })
        mock_get.return_value = mock_response
        self.assertEqual(('Houston', 'TX'),
                         self.locationService.get_zipcode_location('77004'))

    @patch('src.location_service.requests.get')
    def test_get_long_city_name_from_json_data(self, mock_get):
        mock_response = Mock(status_code=200)
        mock_response.json.return_value = (
            {
                "results": [
                    {
                        "address_components": [
                            {
                                "long_name" : "San Francisco",
                                "short_name": "SF",
                                "types": ["locality", "political"]
                            },
                            {
                                "short_name": "CA",
                                "types": ["administrative_area_level_1", "political"]
                            },
                        ],
                    }
                ],
                "status": "OK",
            })
        mock_get.return_value = mock_response
        self.assertEqual(('San Francisco', 'CA'),
                         self.locationService.get_zipcode_location('77004'))
