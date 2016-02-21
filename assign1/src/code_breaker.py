class CodeBreaker():
	def __init__(self):
		self.chances_left = 20

	def setSelection(self, input_selection):
		self.selection = input_selection

	def guess(self, input_guess):
		if self.selection != input_guess:
			return ['White', 'White', 'White', 'White', 'White']
		return ['Black', 'Black', 'Black', 'Black', 'Black']


