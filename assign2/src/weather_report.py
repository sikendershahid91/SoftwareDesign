

class WeatherReport:
    def __init__(self):
        self.zipcode_service = None

    def read_zipcodes(self, read_zipcode): 
        return dict(map(
            lambda x: (x, self.zipcode_service.get_zipcode_location(x)),
            read_zipcode))

    def read_weather(self, read_zipcode):
        return dict(map(
            lambda x: (x, self.zipcode_service.get_zipcode_weather(x)),
            read_zipcode))

    def set_service(self, service):
        self.zipcode_service = service
