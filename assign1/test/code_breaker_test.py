import unittest
from src.code_breaker import CodeBreaker, Color, Response



### so essentially the idea for creating the TDD is to create bit of test then bit of implementation. 
### we want to be testing much more behavior than state of right or wrong. 
### starting from the base would assist in structuring the program 

### example of test 
	### canary, running program - checking environment
	### checkIfplayerIsSet
		### assertTrue(true) case 
	### checkIfcolorPoolcontains10colors 
		### this should help us create a colorPoolClass with stack of 10 colors. 
	### test, pick color place on selection
	
	### aand we can add plenty of negative, exception tests to those postive tests above. YEA FEEL ME DAWG 

class CodeBreakerTest(unittest.TestCase):
	def test_canary(self):
		self.assertTrue(True)

	def setUp(self):
		self.codeBreaker = CodeBreaker()

	def result_of_guess(self, game, selection, guess):
		game.setSelection(selection)
		return game.guess(guess)

	def test_set_selection_with_less_than_5_colors(self):
		selection_set = [Color.black] * 4
		try:
			self.codeBreaker.setSelection(selection_set)
			raise RuntimeError("setSelection accepts less than 5 colors.")
		except ValueError:
			pass

	def test_set_selection_with_more_than_5_colors(self):
		selection_set = [Color.black] * 6
		try:
			self.codeBreaker.setSelection(selection_set)
			raise RuntimeError("setSelection accepts more than 5 colors.")
		except ValueError:
			pass

	def test_set_selection_with_variable_wrong_type(self):
		selection_set = [Color.black] * 4
		selection_set.append(0)
		try:
			self.codeBreaker.setSelection(selection_set)
			raise RuntimeError("setSelection accepts one variable wrong type.")
		except ValueError:
			pass


	def test_guess_with_less_than_5_colors(self):
		selection_set = [Color.black] * 5
		selection_guess = [Color.white] * 4
		try:
			return_response = self.result_of_guess(self.codeBreaker, \
				selection_set, selection_guess)
			raise RuntimeError("guess accepts less than 5 colors.")
		except ValueError:
			pass

	def test_guess_with_more_than_5_colors(self):
		selection_set = [Color.black] * 5
		selection_guess = [Color.white] * 6
		try:
			return_response = self.result_of_guess(self.codeBreaker, \
				selection_set, selection_guess)
			raise RuntimeError("guess accepts more than 5 colors.")
		except ValueError:
			pass
	### irrelevent 
	def test_guess_with_variable_wrong_type(self):
		selection_set = [Color.black] * 5
		selection_guess = [Color.white] * 4
		selection_guess.append('wrong type')
		try:
			return_response = self.result_of_guess(self.codeBreaker, \
				selection_set, selection_guess)
			raise RuntimeError("guess accepts one variable wrong type.")
		except ValueError:
			pass
	
	def test_guess_while_selection_not_set(self):
		selection_guess = [Color.white] * 5
		try:
			return_response = self.codeBreaker.guess(selection_guess)
			raise RuntimeError("Accept guess while selection is not set.")
		except AttributeError:
			pass

	def test_game_all_match_for_correct_guess(self):
		selection_set = [Color.pink, Color.red, Color.green, Color.blue, \
			Color.orange]
		self.assertEqual([Response.MATCH] * 5, self.result_of_guess(\
			self.codeBreaker, selection_set, \
				selection_set))

	def test_game_all_no_match_for_all_different_colors(self):
		selection_set = [Color.pink, Color.red, Color.green, Color.blue, \
			Color.orange]
		selection_guess = [Color.black, Color.white, Color.purple, \
			Color.yellow, Color.silver]
		self.assertEqual([Response.NO_MATCH]*5, self.result_of_guess(\
			self.codeBreaker, selection_set, selection_guess))

	def test_game_all_match_by_position_for_right_color_wrong_positions(self):
		selection_set = [Color.pink, Color.red, Color.green, Color.blue, \
			Color.orange]
		selection_guess = [Color.red, Color.green, Color.blue, Color.orange, \
			Color.pink]
		self.assertEqual([Response.MATCH_POSITION]*5, self.result_of_guess(\
			self.codeBreaker, selection_set, selection_guess))
		

