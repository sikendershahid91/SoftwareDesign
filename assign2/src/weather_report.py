class WeatherReport:
    def __init__(self):
        self.location_service = None
        self.weather_service = None

    def get_cities_and_state(self, zipcodes):
        return dict(map(
            lambda x: (x, self.location_service.get_zipcode_location(x)),
            zipcodes))

    def get_weather_data(self, zipcodes):
        return dict(map(
            lambda x: (x, self.weather_service.get_zipcode_weather(x)),
            zipcodes))

    def get_coldest_city(self, zipcodes):
        return min(
            self.get_weather_data(zipcodes).items(),
            key = lambda x: int(x[1][0])) [0]

    def set_location_service(self, service):
        self.location_service = service

    def set_weather_service(self, service):
        self.weather_service = service
