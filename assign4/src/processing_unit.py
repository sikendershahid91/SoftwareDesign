from functools import reduce

class ProcessingUnit:
    def __init__(self):
        self._blocks = None

    def set_blocks(self, input_blocks):
    	self._blocks = input_blocks

    def process(self, input_string):
    	return reduce(
    		lambda string, block: ''.join(map(block.process, string)),
    		self._blocks,
    		input_string
    		)
