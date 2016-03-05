import unittest
from unittest.mock import MagicMock
# from unittest.mock import patch
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
        self.assertEqual({'city': 'Katy', 'statgie': 'TX'}, self.weatherReport.zipcode_dictionary['77450'])

    def test_read_empty_list_return_empty_dictionary(self):
        zipcode_list = self.weatherReport.read_list.return_value = [" "]
        self.weatherReport.add_zipcode(zipcode_list)
        self.assertEqual({}, self.weatherReport.zipcode_dictionary)


        import unittest
from unittest.mock import patch, Mock
from src.weather_report import WeatherReport, WeatherReportServiceInterface


class WeatherReportTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.weatherReport = WeatherReport()

    def test_read_zipcode_5_digit(self):
        self.weatherReport.read_zipcode(["12345"])
        self.assertEqual({
                    'city': 'empty_data',
                    'state': 'empty_data',
                    'temperature_minimum': 'empty_data',
                    'temperature_maximum': 'empty_data',
                    'weather_condition': 'empty_data',
                }, self.weatherReport.zipcode_dictionary['12345'])

    @patch.object(WeatherReportServiceInterface, 'get_zipcode_location')
    def test_read_one_zipcode_location_when_service_working(self, mock_zipcode_info):
        self.weatherReport.read_zipcode(['77004'])
        mock_zipcode_info.get_zipcode_location.return_value = {'city': 'Houston', 'state': 'TX'}
        self.weatherReport.set_zipcode_location('77004', mock_zipcode_info)
        print(self.weatherReport.zipcode_dictionary['77004']['city'])
        self.assertEqual('Houston', self.weatherReport.zipcode_dictionary['77004']['city'])

    @patch.object(WeatherReportServiceInterface, 'get_zipcode_location')
    def test_read_three_zipcode_location_when_service_working(self, mock_zipcode_info):
        self.weatherReport.read_zipcode(['77004', '90210', '10001'])
        mock_zipcode_info.get_zipcode_location.side_effect = [
            {'city_data': 'Houston', 'state_data': 'TX'},
            {'city_data': 'Beverly Hills', 'state_data': 'CA'},
            {'city_data': 'New York', 'state_data': 'TX'}]
        self.weatherReport.set_zipcode_location('77004', mock_zipcode_info)
        self.weatherReport.set_zipcode_location('90210', mock_zipcode_info)
        self.weatherReport.set_zipcode_location('10001', mock_zipcode_info)
        self.assertEqual(
            {{'city_data': 'Houston', 'state_data': 'TX'},
             {'city_data': 'Beverly Hills', 'state_data': 'CA'},
             {'city_data': 'New York', 'state_data': 'TX'}},
            self.weatherReport.zipcode_dictionary['77004', '90210', '10001'])

    def test_read_0_zipcode_service_not_called(self):
        zipcode_list_to_read = []
        self.assertEqual({}, self.weatherReport.read_zipcode(zipcode_list_to_read))

    @patch.object(WeatherReportServiceInterface, 'get_zipcode_weather')
    def test_read_one_zipcode_weather_when_service_working(self, mock_zipcode_info):
        self.weatherReport.read_zipcode(['77004'])
        mock_zipcode_info.get_zipcode_weather.return_value = {'city_data': 'Houston', 'state_data': 'TX'}
        self.weatherReport.set_zipcode_weather(mock_zipcode_info)
        self.assertEqual({'city_data': 'Houston', 'state_data': 'TX'}, self.weatherReport.zipcode_dictionary['77004'])

    @patch.object(WeatherReportServiceInterface, 'get_zipcode_weather')
    def test_read_three_zipcode_weather_when_service_working(self, mock_zipcode_info):
        self.weatherReport.read_zipcode(['77004', '90210', '10001'])
        mock_zipcode_info.get_zipcode_weather.side_effect = [
            {'temperature_minimum': '20', 'temperature_maximum': '25', 'weather_condition': 'Mostly Sunny'},
            {'temperature_minimum': '25', 'temperature_maximum': '30', 'weather_condition': 'Sunny'},
            {'temperature_minimum': '30', 'temperature_maximum': '40', 'weather_condition': 'Partially Sunny'}]
        self.weatherReport.set_zipcode_weather(mock_zipcode_info)
        self.assertEqual(
            {{'temperature_minimum': '20', 'temperature_maximum': '25', 'weather_condition': 'Mostly Sunny'},
             {'temperature_minimum': '20', 'temperature_maximum': '25', 'weather_condition': 'Mostly Sunny'},
             {'temperature_minimum': '20', 'temperature_maximum': '25', 'weather_condition': 'Mostly Sunny'}},
            self.weatherReport.zipcode_dictionary['77004', '90210', '10001'])



