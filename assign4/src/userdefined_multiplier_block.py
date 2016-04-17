class userdefinedMultiplierBlock:

    def factor_setup(self, input_char):
        self._factor = int(input_char)

    def process(self, input):
        return str(input) * self._factor
