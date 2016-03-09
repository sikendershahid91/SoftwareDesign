class WeatherReport:
    def __init__(self):
        self._location_service = None
        self._weather_service = None

    def get_cities_and_state(self, zipcodes):
        return dict(map(
            lambda zipcode: (zipcode, 
                self._location_service.get_zipcode_location(zipcode)),
            zipcodes))

    def get_weather_data(self, zipcodes):
        return dict(map(
            lambda zipcode: (zipcode, 
                self._weather_service.get_zipcode_weather(zipcode)),
            zipcodes))

    def get_coldest_city(self, zipcodes):
        return min(
            self.get_weather_data(zipcodes).items(),
            key = lambda weather_data: int(weather_data[1][0])) [0]

    def get_hottest_city(self, zipcodes):
        return max(
            self.get_weather_data(zipcodes).items(),
            key = lambda weather_data: int(weather_data[1][1])) [0]

    def set_location_service(self, service):
        self._location_service = service

    def set_weather_service(self, service):
        self._weather_service = service
