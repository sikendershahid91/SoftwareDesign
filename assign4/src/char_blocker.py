class CharBlock:
    def __init__(self, char = ''):
        self._char = char

    def case_setup(self, input_char):
        self._char = input_char

    def process(self, input):
        return '' if input == self._char else input
