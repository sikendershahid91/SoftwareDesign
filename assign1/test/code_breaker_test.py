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

    def test_game_all_match_for_right_color_wrong_positions(self):
        selection_set = [Color.pink, Color.red, Color.green, Color.blue, Color.orange]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.red, Color.green, Color.blue, Color.orange, Color.pink]
        self.assertEqual([Response.MATCH] * 5, self.codeBreaker.evaluate_guess(selection_guess))

    def test_game_match_and_wrong_position_match_and_no_match(self):
        selection_set = [Color.black, Color.black, Color.purple, Color.green, Color.red]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.black, Color.black, Color.green, Color.purple, Color.blue]
        self.assertEqual([Response.NO_MATCH, Response.MATCH, Response.MATCH, Response.MATCH_POSITION,
                          Response.MATCH_POSITION], self.codeBreaker.evaluate_guess(selection_guess))

    def test_game_color_twice_no_repeated_colors(self):
        selection_set = [Color.black, Color.green, Color.blue, Color.red, Color.pink]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.black, Color.green, Color.blue, Color.red, Color.black]
        self.assertEqual([Response.NO_MATCH, Response.MATCH_POSITION, Response.MATCH_POSITION, Response.MATCH_POSITION,
                          Response.MATCH_POSITION], self.codeBreaker.evaluate_guess(selection_guess))

    def test_game_color_twice_match_and_match_by_position(self):
        selection_set = [Color.black, Color.green, Color.black, Color.red, Color.pink]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.black, Color.green, Color.pink, Color.red, Color.black]
        self.assertEqual([Response.MATCH, Response.MATCH, Response.MATCH_POSITION, Response.MATCH_POSITION,
                          Response.MATCH_POSITION], self.codeBreaker.evaluate_guess(selection_guess))

    def test_guess_two_repeated_wrong_position_color_with_one_match(self):
        selection_set = [Color.pink, Color.green, Color.black, Color.red, Color.blue]
        self.codeBreaker.set_selected_colors(selection_set)
        selection_guess = [Color.black, Color.orange, Color.purple, Color.yellow, Color.black]
        print(self.codeBreaker.evaluate_guess(selection_guess))
        self.assertEqual([Response.NO_MATCH, Response.NO_MATCH, Response.NO_MATCH, Response.NO_MATCH,
                          Response.MATCH], self.codeBreaker.evaluate_guess(selection_guess))
