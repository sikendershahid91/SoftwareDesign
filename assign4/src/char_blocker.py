class CharBlock:
    

    def __init__(self, char):
        self._char = char


    def process(self, input):
        return '' if input == self._char else input


    @classmethod
    def handle_string(cls, string):
        splited_string = string.split('-')
        if (len(splited_string) == 2 and
          splited_string[1] == 'blocker' and
          len(splited_string[0]) == 1):
            return  cls(splited_string[0])
        return None