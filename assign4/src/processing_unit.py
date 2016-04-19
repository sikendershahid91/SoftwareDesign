from functools import reduce

class ProcessingUnit:
    def __init__(self): #Venkat: Take a list of blocks in the constructor
        self._blocks = None

    def set_blocks(self, input_blocks): #Venkat: Remove this function
    	self._blocks = input_blocks

    def process(self, input_string): #Venkat: Nice work here.
    	return reduce(
    		lambda string, block: ''.join(map(block.process, string)),
    		self._blocks,
    		input_string
    		)
