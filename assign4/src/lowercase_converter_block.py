class LowerCaseConverterBlock:


    def process(self, input):
        return input.lower()


    @classmethod
    def handle_string(cls, string):
        return cls() if string == 'LowerCaseConverter' else None

