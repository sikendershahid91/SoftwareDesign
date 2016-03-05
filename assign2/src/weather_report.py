

class WeatherReport:
    def __init__(self):
        self.zipcode_service = None
        self.zipcode_location_dictionary = {}

    def read_zipcodes(self, read_zipcode):
        for zipcode in read_zipcode:
            if len(zipcode) != 5 or not(zipcode.isdigit()):
                raise ValueError('Error: Invalid Zipcode')
            else:
                self.set_zipcode_location(zipcode)
                self.set_zipcode_weather(zipcode)
        return self.zipcode_location_dictionary

    def set_location_service(self, service):
        self.zipcode_service = service

    def set_zipcode_location(self, zipcode):
        self.zipcode_location_dictionary[zipcode] = (self.zipcode_service.get_zipcode_location(zipcode))

    def set_zipcode_weather(self, zipcode):
        self.zipcode_location_dictionary[zipcode] = (self.zipcode_service.get_zipcode_weather(zipcode))
