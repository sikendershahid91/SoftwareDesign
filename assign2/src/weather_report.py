class WeatherReport:
    def __init__(self):
        self.zipcode_service = None

    def read_zipcodes(self, read_zipcode): #Venkat: change to get_cities_and_state. Change parameter to zipcodes
        return dict(map(
            lambda x: (x, self.zipcode_service.get_zipcode_location(x)),
            read_zipcode))

    def read_weather(self, read_zipcode): #Venkat: change to get_weather_data. Change parameter to zipcodes
        return dict(map(
            lambda x: (x, self.zipcode_service.get_zipcode_weather(x)),
            read_zipcode))
#Venkat: The weather data should come from a different service than the citie and states details. SRP.
    def set_service(self, service):
        self.zipcode_service = service
