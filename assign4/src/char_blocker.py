class CharBlock:
    def __init__(self, char):
        self._char = char

    def process(self, input):
        return '' if input == self._char else input
