from enum import Enum
import random


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
    raw_umber = 10
    fuchsia = 11
    cadet_blue = 12
    copper = 13


class Response(Enum):
    NO_MATCH = 0
    MATCH = 1
    MATCH_POSITION = 2


class CodeBreaker:
    def __init__(self):
        self.selected_colors = []
        self.number_of_guess_made = 0
        self.game_won = False
        self.color_pool = [Color.copper, Color.cadet_blue, Color.fuchsia, 
        Color.red, Color.green, Color.blue, Color.pink, Color.yellow, 
        Color.pink, Color.orange, Color.purple]

    def set_colors_selection(self, input_selection):
        if len(input_selection) != 5:
            raise (ValueError('Not exactly 5 colors.'))
        self.selected_colors = input_selection

    def random_colors_selection(self):
        self.selected_colors = random.sample(self.color_pool*5, 5)

    def guess_colors(self, input_guess):
        if len(input_guess) != 5:
            raise (ValueError('Not exactly 5 colors.'))
        response = []
        left_over_selection_color = []
        left_over_guess_color = []
        for i in range(5):
            if self.selected_colors[i] == input_guess[i]:
                response.append(Response.MATCH_POSITION)
            else:
                left_over_selection_color.append(self.selected_colors[i])
                left_over_guess_color.append(input_guess[i])
        for color in left_over_guess_color:
            if color in left_over_selection_color:
                response.append(Response.MATCH)
                left_over_selection_color.remove(color)
            else:
                response.append(Response.NO_MATCH)
        response.sort(key=lambda x: x.value)

        self.number_of_guess_made += 1
        if self.number_of_guess_made <= 20 and response == [Response.MATCH_POSITION]*5:
            self.game_won = True

        return response
