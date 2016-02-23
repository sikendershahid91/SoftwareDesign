import unittest
from src.code_breaker import CodeBreaker, Color, Response


class CodeBreakerTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def setUp(self):
        self.codeBreaker = CodeBreaker()

    def select_first_color(self):
        self.codeBreaker.select_color(Color.black)
        self.assertEqual(Color.black, self.codeBreaker.selected_colors[0])

    def test_guess_less_than_5_selection(self):
        self.codeBreaker.select_color(Color.black)
        self.codeBreaker.select_color(Color.white)
        self.codeBreaker.select_color(Color.silver)
        try:
            self.codeBreaker.evaluate_guess(self.codeBreaker.selected_colors)
            raise RuntimeError("guess accepts less than 5 colors.")
        except ValueError:
            pass

    def test_guess_with_more_than_5_colors(self):
        selection_set = [Color.black] * 6
        try:
            self.codeBreaker.evaluate_guess(selection_set)
            raise RuntimeError("guess accepts more than 5 colors.")
        except ValueError:
            pass

    def test_all_match_for_correct_guess(self):
        selection_set = [Color.pink, Color.red, Color.green, Color.blue, Color.orange]
        self.codeBreaker.set_selected_colors(selection_set)
        self.assertEqual([Response.MATCH_POSITION] * 5, self.codeBreaker.evaluate_guess(selection_set))

    def test_game_all_no_match_for_all_different_colors(self):
        selection_set = [Color.pink, Color.red, Color.green, Color.blue, Color.orange]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.black, Color.white, Color.purple, Color.yellow, Color.silver]
        self.assertEqual([Response.NO_MATCH] * 5, self.codeBreaker.evaluate_guess(selection_guess))

    def test_game_all_match_by_position_for_right_color_wrong_positions(self):
        selection_set = [Color.pink, Color.red, Color.green, Color.blue, Color.orange]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.red, Color.green, Color.blue, Color.orange, Color.pink]
        self.assertEqual([Response.MATCH] * 5, self.codeBreaker.evaluate_guess(selection_guess))


