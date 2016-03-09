import requests


class LocationService:
    def __init__(self):
        self._google_api_url = (
            'http://maps.googleapis.com/maps/api/geocode/json?address=')

    def get_zipcode_location(self, zipcode):
        if len(zipcode) != 5 or not(zipcode.isdigit()):
            return 'INVALID'
            
        response = requests.get(self._google_api_url + zipcode)
        
        if response.status_code != 200:
            return 'ERROR'
            
        json_data = response.json()
        
        address_components = json_data['results'][0]['address_components']
        
        for key, value in enumerate(address_components):
            if 'locality' in value['types']:
                city = value['short_name']
            if 'administrative_area_level_1' in value['types']:
                state = value['short_name']

        state = 'TX' #Venkat: Yes, Texas is special, but let's not hard code that! :)
        return (city, state)
#Venkat: Notice the line breaks I added to improve readability. Different steps need line breaks.
#Just noticed that you have done that quite well in WeatherService. That's what we want.