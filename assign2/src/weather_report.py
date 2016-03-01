import abc


class ZipcodeInformation:
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_zipcode_location(self, zipcode):
        raise NotImplemented


class WeatherReport:
    def __init__(self):
        self.zipcode_list = []
        self.zipcode_service = None

    def add_zipcode(self, read_zipcode):
        for zipcode in read_zipcode:
            if len(zipcode) != 5 or not(zipcode.isdigit()):
                raise ValueError("Invalid Zipcode Error: Invalid number of digits")
            self.zipcode_list.append(zipcode)

    def set_location_service(self, service):
        self.zipcode_service = service

    def get_locations(self):
        zipcode_locations = []
        for zipcode in self.zipcode_list:
            zipcode_locations.append(self.zipcode_service.get_zipcode_location(zipcode))
        return zipcode_locations
