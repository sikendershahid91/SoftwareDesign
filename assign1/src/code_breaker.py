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
    MATCH_POSITION = 0
    MATCH = 1
    NO_MATCH = 2


class Status(Enum):
    WIN = 0
    LOSE = 1
    CONTINUE = 2


class CodeBreaker:
    def __init__(self):
        self.selected_colors = []
        self.number_of_guess_made = 0
        self.game_status = Status.CONTINUE

    def set_colors_selection(self, input_selection):
        if len(input_selection) != 5:
            raise (ValueError('Not exactly 5 colors.'))
        self.selected_colors = input_selection

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
            self.game_status = Status.WIN
        elif self.number_of_guess_made >= 20:
            self.game_status = Status.LOSE

        return response
