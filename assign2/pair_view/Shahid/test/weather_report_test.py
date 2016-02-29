import unittest
import unittest.mock
from src.weather_report import WeatherReport


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()

    def test_read_zipcode_5_digit(self):
        self.assertEqual(['12345'], self.weatherReport.add_zipcode(["12345"]))

    def test_read_zipcode_not_5_digit_exception(self):
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["123456"])

    def test_read_more_than_one_zipcode(self):
        self.assertEqual(['12345', '54321'], self.weatherReport.add_zipcode(["12345", "54321"]))

    def test_read_zipcode_alphanumeric_type_exception(self):
        self.assertRaises(ValueError, self.weatherReport.add_zipcode, ["aa&12"])


