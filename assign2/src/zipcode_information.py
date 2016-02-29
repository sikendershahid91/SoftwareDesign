import requests


class ZipCodeInformation:
    def __init__(self):
        self.zipcode = ""
        self.google_zipcode_api = (
            "http://maps.googleapis.com/maps/api/geocode/json?address=ZIPCODE")

    def set_zipcode(self, input_zipcode):
        if (len(input_zipcode) == 5 and
            all(char in '0123456789' for char in input_zipcode)):
            self.zipcode = input_zipcode
        else:
            self.zipcode = ""

    def get_city(self):
        response = requests.get(self.google_zipcode_api + self.zipcode)
        data = response.json()
        for item in data['results'][0]["address_components"]:
            if "locality" in item["types"]:
                return item["long_name"]
        return

    def get_state(self):
        response = requests.get(self.google_zipcode_api + self.zipcode)
        data = response.json()
        for item in data['results'][0]["address_components"]:
            if "administrative_area_level_1" in item["types"]:
                return item["short_name"]
        return