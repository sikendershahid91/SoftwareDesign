import unittest
import src.code_breaker

class CodeBreakerTest(unittest.TestCase):
	def test_canary(self):
		self.assertTrue(True)

	def setUp(self):
		self.codeBreaker = src.code_breaker.CodeBreaker()

	def tearDown(self):
		pass

	def test_new_game_has_20_chances(self):
		self.assertEqual(20, self.codeBreaker.chances_left)

	def result_of_guess(self, game, selection, guess):
		game.setSelection(selection)
		return game.guess(guess)

	def test_game_return_5_blacks_for_correct_guess(self):
		selection_set = ['Pink', 'Red', 'Green', 'Blue', 'Orange']
		self.assertEqual(['Black', 'Black', 'Black', 'Black', 'Black'], \
			self.result_of_guess(self.codeBreaker, selection_set, \
				selection_set))

	def test_game_return_5_whites_for_all_wrong_guess(self):
		selection_set = ['Pink', 'Red', 'Green', 'Blue', 'Orange']
		selection_guess = ['Black', 'White', 'Purple', 'Yellow', 'Silver']
		self.assertEqual(['White', 'White', 'White', 'White', 'White'], \
			self.result_of_guess(self.codeBreaker, selection_set,  selection_guess))

		

