

class WeatherReport:
    def __init__(self):
        self.zipcode_service = None
        self.zipcode_location_dictionary = {} #Venkat: Remove avoid state

    def read_zipcodes(self, read_zipcode): #Venkat:  change to get_cities_and_states
#Venkat: use the map function and lambda instead of for.
        for zipcode in read_zipcode:
            if len(zipcode) != 5 or not(zipcode.isdigit()):
                raise ValueError('Error: Invalid Zipcode') #Venkat: Don't check for length, fails SRP for this function. If the service reports that the zip code is invalid, then capture that detail as error
            else:
                self.set_zipcode_location(zipcode) #Venkat: Don't store, collect into a list instead and return 
                self.set_zipcode_weather(zipcode)
        return self.zipcode_location_dictionary

    def set_location_service(self, service):
        self.zipcode_service = service

    def set_zipcode_location(self, zipcode):
        self.zipcode_location_dictionary[zipcode] = (self.zipcode_service.get_zipcode_location(zipcode))

    def set_zipcode_weather(self, zipcode):
        self.zipcode_location_dictionary[zipcode] = (self.zipcode_service.get_zipcode_weather(zipcode))
