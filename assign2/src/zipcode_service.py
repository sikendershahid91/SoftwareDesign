
class ZipcodeService:

    def get_zipcode_location(self, zipcode):
        if len(zipcode) != 5 or not(zipcode.isdigit()):
        	return 'INVALID'

    def get_zipcode_weather(self, zipcode):
        raise NotImplemented
