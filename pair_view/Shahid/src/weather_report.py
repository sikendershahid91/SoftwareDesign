import abc


class ZipcodeInformation:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_zipcode_location(self, zipcode):
        raise NotImplemented


class WeatherReport:
    def __init__(self):
        self.zipcode_dictionary = {}

    def add_zipcode(self, read_zipcode):
        for zipcode in read_zipcode:
            if zipcode == " ":
                continue
            if len(zipcode) != 5 or not(zipcode.isdigit()):
                raise ValueError("Invalid Zipcode Error: Invalid number of digits")
            else:
                self.zipcode_dictionary = {zipcode: {
                'city': 'empty_data', 
                'state': 'empty_data',
                'temperature_minimum': 'empty_data',
                'temperature_maximum': 'empty_data',
                'weather_condition': 'empty_data',
                }}
        return self.zipcode_dictionary
 
    def read_list(self):
        pass

    def set_zipcode(self, zipcode, zipcode_data):
        if zipcode != " ":
            self.zipcode_dictionary[zipcode] = zipcode_data



class WeatherReportServiceInterface:
    def get_zipcode_weather(self, zipcode):
        pass

    def get_zipcode_location(self, zipcode):
        pass


class WeatherReport:
    def __init__(self):
        self.zipcode_service = None
        self.zipcode_dictionary = {}

    def read_zipcode(self, input_zipcode_list):
        for zipcode in input_zipcode_list:
            if len(zipcode) != 5 or not (zipcode.isdigit()):
                raise ValueError(
                    "Invalid Zipcode Error: Invalid number of digits")
            else:
                self.zipcode_dictionary = {zipcode: {
                    'city': 'empty_data',
                    'state': 'empty_data',
                    'temperature_minimum': 'empty_data',
                    'temperature_maximum': 'empty_data',
                    'weather_condition': 'empty_data',
                }}
        return self.zipcode_dictionary

    def set_zipcode_location(self, zipcode, zipcode_location):
        self.zipcode_dictionary[zipcode]['city'] = zipcode_location['city']
        self.zipcode_dictionary[zipcode]['state'] = zipcode_location['state']

    def set_zipcode_weather(self, zipcode, zipcode_weather):
        self.zipcode_dictionary[zipcode]['temperature_minimum'] = zipcode_weather['temperature_minimum']
        self.zipcode_dictionary[zipcode]['temperature_maximum'] = zipcode_weather['temperature_maximum']
        self.zipcode_dictionary[zipcode]['weather_condition'] = zipcode_weather['weather_condition']

        # self.zipcode_dictionary[zipcode] = (
        #                     self.zipcode_service.get_zipcode_location(zipcode))
        #                 self.zipcode_dictionary[zipcode] = (
        #                     self.zipcode_service.get_zipcode_weather(zipcode))

