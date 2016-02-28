class ZipCodeInformation:
	def __init__(self):
		self.zipcode = ""

	def set_zipcode(self, input_zipcode):
		if len(input_zipcode) == 5 and not any(char not in '0123456789' for char in input_zipcode):  
			self.zipcode = input_zipcode
		else:
			self.zipcode = ""
		
