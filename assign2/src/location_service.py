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
        
        for component in address_components:
            if 'locality' in component['types']:
                city = component['long_name']
            if 'administrative_area_level_1' in component['types']:
                state = component['short_name']

        return (city, state)
