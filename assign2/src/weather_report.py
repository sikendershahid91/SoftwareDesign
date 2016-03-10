class WeatherReport:
    def __init__(self):
        self._location_service = None
        self._weather_service = None

    def get_cities_and_state(self, zipcode_list):
        return dict(map(
            lambda zipcode: (zipcode,
                             self._location_service.get_zipcode_location(zipcode)),
            zipcode_list))

    def get_weather_data(self, zipcode_list):
        return dict(map(
            lambda zipcode: (zipcode,
                             self._weather_service.get_zipcode_weather(zipcode)),
            zipcode_list))

    def get_all_data(self, zipcode_list):
        return dict(map(
            lambda zipcode: (zipcode,
                             self._location_service.get_zipcode_location(zipcode) +
                             self._weather_service.get_zipcode_weather(zipcode)), zipcode_list))

    def get_coldest_city(self, zipcode_list):
        return min(self.get_weather_data(zipcode_list).items(), key=lambda weather_data: int(weather_data[1][0]))[0]

    def get_hottest_city(self, zipcode_list):
        return max(self.get_weather_data(zipcode_list).items(), key=lambda weather_data: int(weather_data[1][1]))[0]

    def set_location_service(self, service):
        self._location_service = service

    def set_weather_service(self, service):
        self._weather_service = service
