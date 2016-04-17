class userdefinedCaseConvertorBlock:

	def case_setup(self, input_char):
		self._char = input_char

	def process(self, input):
		if input == self._char:
			return input.swapcase()
		else:
			return input
