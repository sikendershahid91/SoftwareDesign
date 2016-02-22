from enum import Enum

class Color(Enum):   ### for now i think should keep the essential colors black, silver, white
	black = 0    ### perform tests to see if the response for two main cases works 
	white = 1    ###  case 1: response for all win, response for all wrong
	silver = 2
	red = 3
	green = 4    ### i was thinking about the color and the rgb value, ... notice in venkat's lecture
	blue = 5     ### for the tic tac toe, he cared about the "X" and "O" case at the very end. 
	pink = 6     ### only essential thing about the color pool should be right is distinction. 
	yellow = 7   ###  test to see if color pool contains 10 distinctive colors. 
	orange = 8   ###  represent the colors with decimal digits at the moment
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


