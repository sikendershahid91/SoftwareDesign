import unittest
from unittest.mock import patch, Mock
from src.location_service import LocationService

class LocationServiceTest(unittest.TestCase):

    def setUp(self):
        self.locationService = LocationService()

    # @patch.object(LocationService, 'get_zipcode_location')
    # def test_read_one_zipcode_location_when_service_working(
    #         self, mock_location):
    #     zipcode_list_to_read = ['77004']
    #     mock_location.get_zipcode_location.return_value = ('Houston', 'TX')
    #     self.weatherReport.set_location_service(mock_location)
    #     self.assertEqual({'77004': ('Houston', 'TX')}, 
    #         self.weatherReport.get_cities_and_state(zipcode_list_to_read))

    def test_get_invalid_from_service_for_wrong_zipcode_digit(self):
        self.assertEqual('INVALID', 
            self.locationService.get_zipcode_location('a2342'))

    def test_get_invalid_from_service_for_wrong_zipcode_length(self):
        self.assertEqual('INVALID', 
            self.locationService.get_zipcode_location('122342'))

    @patch('src.location_service.requests.get')
    def test_not_succesful_http_connection_output(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.response = mock_response
        self.assertEqual('ERROR', 
            self.locationService.get_zipcode_location('77004'))

    @patch('src.location_service.requests.get')
    def test_get_correct_location_from_successful_json_data(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = (
            {
                "results" : [
                     {
                        "address_components" : [
                            {
                                "short_name" : "Houston",
                                "types" : [ "locality", "political" ]
                            },
                            {
                                "short_name" : "TX",
                                "types" : [ "administrative_area_level_1", "political" ]
                            },
                        ],
                    }
                ],
                "status" : "OK",
            })
        mock_get.response = mock_response
        self.assertEqual(('Houston', 'TX'), 
            self.locationService.get_zipcode_location('77004'))





