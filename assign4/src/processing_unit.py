from functools import reduce


class ProcessingUnit:


    def __init__(self, blocks):
        self._blocks = blocks


    def process(self, input_string):
    	return reduce(
    	  lambda string, block: ''.join(map(block.process, string)),
    	  self._blocks,
    	  input_string
    	)
