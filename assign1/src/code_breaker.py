from enum import Enum

class Color(Enum):
	black = 0
	white = 1
	silver = 2
	red = 3
	green = 4
	blue = 5
	pink = 6
	yellow = 7
	orange = 8
	purple = 9

class Response(Enum):
	MATCH = 0
	MATCH_POSITION = 1
	NO_MATCH = 2

class CodeBreaker():


	def __init__(self):
		self.chances_left = 20

	def _check_color_selection_type(self, input_selection):
		if len(input_selection) != 5:
			raise(ValueError('Not exactly 5 colors.'))
		for i in range(5):
			if type(input_selection[i]) != Color:
				raise(ValueError('Input selection member is not Color type.'))
		return

	def setSelection(self, input_selection):
		self._check_color_selection_type(input_selection) 
		self.selection = input_selection

	def guess(self, input_guess):
		self._check_color_selection_type(input_guess)
		if self.selection != input_guess:
			key_sort_func = lambda x: x.value
			if sorted(self.selection, key = key_sort_func) \
				== sorted(input_guess, key = key_sort_func):
				return [Response.MATCH_POSITION] * 5
			return [Response.NO_MATCH] * 5
		return [Response.MATCH] * 5


