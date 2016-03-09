class WeatherReport:
    def __init__(self):
        self.location_service = None
        self.weather_service = None

    def get_cities_and_state(self, zipcodes): #Venkat: change to get_cities_and_state. Change parameter to zipcodes
        return dict(map(
            lambda x: (x, self.location_service.get_zipcode_location(x)),
            zipcodes))

    def get_weather_data(self, zipcodes): #Venkat: change to get_weather_data. Change parameter to zipcodes
        return dict(map(
            lambda x: (x, self.weather_service.get_zipcode_weather(x)),
            zipcodes))
#Venkat: The weather data should come from a different service than the citie and states details. SRP.
    def set_location_service(self, service):
        self.location_service = service

    def set_weather_service(self, service):
        self.weather_service = service
