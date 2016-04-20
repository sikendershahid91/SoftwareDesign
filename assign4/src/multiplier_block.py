class MultiplierBlock:


    def process(self, input):
        return str(input) * 2


    @classmethod
    def handle_string(cls, string):
        return cls() if string == 'Multiplier' else None
