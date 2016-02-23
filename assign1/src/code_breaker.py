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
        self.selected_colors = []
        self.chances_left = 20

    @staticmethod
    def _check_color_selection_type(input_selection):
        if len(input_selection) != 5:
            raise (ValueError('Not exactly 5 colors.'))
        return

    def set_selected_colors(self, input_selection):
        self._check_color_selection_type(input_selection)
        self.selected_colors = input_selection

    def evaluate_guess(self, input_guess):
        self._check_color_selection_type(input_guess)
        if self.selected_colors != input_guess:
            key_sort_func = lambda x: x.value
            if sorted(self.selected_colors, key=key_sort_func) == sorted(input_guess, key=key_sort_func):
                return [Response.MATCH_POSITION] * 5
            return [Response.NO_MATCH] * 5
        return [Response.MATCH] * 5

    def select_color(self, param):
        self.selected_colors.append(param)
        return self.selected_colors[0]
