class ZipcodeService:

    def get_zipcode_location(self, zipcode):
        if len(zipcode) != 5 or not(zipcode.isdigit()):
        	return 'INVALID'
#Venkat: Write a separate test file for testing this function and only then implement.

    def get_zipcode_weather(self, zipcode): #Venkat: This should not be here, fails SRP. Should be in a separate class
        raise NotImplemented
