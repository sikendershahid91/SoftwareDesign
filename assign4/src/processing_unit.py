class ProcessingUnit:
    def __init__(self):
        block_char = CharBlock()

    def char_blocker(self, blocking_char, input_char):
        block_char.case_setup(blocking_char)
        block_char.process(input_char)
