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
        self.response = [] #Venkat: Remove from the class
        self.number_of_chances_left = 20

    @staticmethod #Venkat: static is not a good idea. Make these instance methods
    def _check_type_color(input_color): #Venkat: Remove
        if type(input_color) != Color:
            raise (ValueError("Not true color type."))

    @staticmethod
    def _check_color_selection_type(input_selection):  #Venkat: Remove
        if len(input_selection) != 5:
            raise (ValueError('Not exactly 5 colors.'))
        return

    def set_selected_colors(self, input_selection):
        self._check_color_selection_type(input_selection)
        self.selected_colors = input_selection

    def match(self, input_guess):
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

    def guess(self, input_guess): #Venkat: Remove
        self.number_of_chances_left -= 1
        if self.number_of_chances_left < 0:
            raise ValueError
        return self.match(input_guess)

    def color_selection(self, param):  #Venkat: Remove
        self._check_type_color(param)
        self.selected_colors.append(param)
