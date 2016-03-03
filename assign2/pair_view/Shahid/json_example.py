import json
import requests


class ZipcodeInformation:
    def __init__(self):
        self.google_location_api = "http://maps.googleapis.com/maps/api/geocode/json"
        self.zipcode_dictionary = {}

    def add_zipcode(self, zipcode):
        self.zipcode_dictionary = {zipcode: {'city': 'city_data', 'state': 'state_data'}}

    def get_zipcode_location(self, zipcode):
        param = dict(address=zipcode)
        json_data = requests.get(self.google_location_api, params=param)
        data = json_data.json()
        address_components = data['results']
        address_components_dictionary = dict(address_components[0])
        city_name, state_name = "", ""
        for item in address_components_dictionary.get('address_components'):
            if 'locality' in item['types']:
                city_name = item['long_name']
            if 'administrative_area_level_1' in item['types']:
                state_name = item['short_name']
        self.zipcode_dictionary[zipcode] = {'city': city_name, 'state': state_name}

if __name__ == "__main__":
    check = ZipcodeInformation()
    check.add_zipcode("77498")
    check.add_zipcode("77074")
    check.get_zipcode_location("77498")
    check.get_zipcode_location("77074")
    print(check.zipcode_dictionary)

    # output
    # {'77074': {'state': 'TX', 'city': 'Houston'}, '77498': {'state': 'TX', 'city': 'Sugar Land'}}




