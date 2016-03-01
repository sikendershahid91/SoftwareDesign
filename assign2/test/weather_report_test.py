import unittest
from unittest.mock import patch
from src.weather_report import WeatherReport, ZipcodeInformation


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()

    def test_read_zipcode_5_digit(self):
        self.weatherReport.add_zipcode(["12345"])
        self.assertEqual(['12345'], self.weatherReport.zipcode_list)

    def test_read_zipcode_not_5_digit_exception(self):
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["123456"])

    def test_read_more_than_one_zipcode(self):
        self.weatherReport.add_zipcode(["12345", "54321"])
        self.assertEqual(['12345', '54321'], self.weatherReport.zipcode_list)

    def test_read_zipcode_alphanumeric_type_exception(self):
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["aa&12"])

    @patch.object(ZipcodeInformation, 'get_zipcode_location')
    def test_zipcode_location_Houston_when_service_working(self, mock_zipcode_info):
        self.weatherReport.add_zipcode(['77004'])
        mock_zipcode_info.get_zipcode_location.return_value = 'Houston'
        self.weatherReport.set_location_service(mock_zipcode_info)
        self.assertEqual(['Houston'], self.weatherReport.get_locations())


