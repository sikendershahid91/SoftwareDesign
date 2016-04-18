class CharBlock:

    def case_setup(self, input_char):
        self._char = input_char

    def process(self, input):
        return '' if input ==self._char else input
