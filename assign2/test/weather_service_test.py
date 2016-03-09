import unittest
from unittest.mock import patch, Mock
from src.weather_service import WeatherService


class LocationServiceTest(unittest.TestCase):

    def setUp(self):
        self.weatherReport = WeatherReport()
        self.weatherService = WeatherService()