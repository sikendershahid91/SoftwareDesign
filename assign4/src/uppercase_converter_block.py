class UpperCaseConverterBlock:


    def process(self, input):
        return input.upper()


    @classmethod
    def handle_string(cls, string):
        return cls() if string == 'UpperCaseConverter' else None
