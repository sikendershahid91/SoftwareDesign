import requests
import xml.etree.ElementTree as ET

class WeatherService:
    def __init__(self):
        self._weather_gov_url = (
            'http://graphical.weather.gov/xml/sample_products/browser_interface'
            '/ndfdBrowserClientByDay.php?'
            'format=24+hourly&numDays=1&zipCodeList=')

    def get_zipcode_weather(self, zipcode):
        if len(zipcode) != 5 or not(zipcode.isdigit()):
            return 'INVALID'

        response = requests.get(self._weather_gov_url + zipcode)
        if response.status_code != 200:
            return 'ERROR'

        tree_data = ET.fromstring(response.content)

        for condition in tree_data.iter('weather-conditions'):
            weather_condition = condition.attrib['weather-summary']

        maximum_temp = 0
        minimum_temp = 0
        for temperature in tree_data.iter('temperature'):
            if temperature.attrib['type'] == 'maximum':
                maximum_temp = temperature.find('value').text
            if temperature.attrib['type'] == 'minimum':
                minimum_temp = temperature.find('value').text

        return (minimum_temp, maximum_temp, weather_condition)


