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
                self.zipcode_dictionary = {zipcode: {'city': 'empty_data', 'state': 'empty_data'}}
        return self.zipcode_dictionary

    def read_list(self):
        pass

    def set_zipcode(self, zipcode, zipcode_data):
        if zipcode != " ":
            self.zipcode_dictionary[zipcode] = zipcode_data

