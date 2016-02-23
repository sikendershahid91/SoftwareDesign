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
    MATCH_POSITION = 2
    MATCH = 1
    NO_MATCH = 0


class CodeBreaker():
    def __init__(self):
        self.selected_colors = []
        self.response = []

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
        self.response = []
        left_over_selection_color = []
        left_over_guess_color = []
        for i in range(5):
            if self.selected_colors[i] == input_guess[i]:
                self.response.append(Response.MATCH_POSITION)
            else:
                left_over_selection_color.append(self.selected_colors[i])
                left_over_guess_color.append(input_guess[i])
        for color in left_over_guess_color:
            if color in left_over_selection_color:
                self.response.append(Response.MATCH)
                left_over_selection_color.remove(color)
            else:
                self.response.append(Response.NO_MATCH)
        self.response.sort(key=lambda x: x.value)
        return self.response

    def select_color(self, param):
        self.selected_colors.append(param)
        return self.selected_colors[0]
