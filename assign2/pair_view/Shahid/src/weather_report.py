

class WeatherReport:
    def __init__(self):
        self.zipcode_list = []

    def add_zipcode(self, read_zipcode):
        for zipcode in read_zipcode:
            if len(zipcode) != 5 or not(zipcode.isdigit()):
                raise ValueError("Invalid Zipcode Error: Invalid number of digits")
            else:
                self.zipcode_list.append(zipcode)
        return self.zipcode_list
