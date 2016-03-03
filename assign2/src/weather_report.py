import abc


class ZipcodeInformation:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_zipcode_location(self, zipcode):
        raise NotImplemented


class WeatherReport:
    def __init__(self):
        self.location_service = None
        self.zipcode_location_dictionary = {}

    def read_zipcodes(self, read_zipcode):
        for zipcode in read_zipcode:
            if len(zipcode) != 5 or not(zipcode.isdigit()):
                raise ValueError(
                    "Invalid Zipcode Error: Invalid number of digits")
            else:
                self.zipcode_location_dictionary[zipcode] = (
                    self.location_service.get_zipcode_location(zipcode))
        return self.zipcode_location_dictionary

    def set_location_service(self, service):
        self.location_service = service

