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
        

    @classmethod
    def block_parser(cls, available_blocks, string):
        for block in available_blocks:
            output_block = block.handle_string(string)
            if output_block:
                return output_block
        raise ValueError('Unable to parse block type from {}'.format(string))


    @classmethod
    def from_string_factory(cls, available_blocks, string_of_blocks):
        unit = cls(list(map(
            lambda string: cls.block_parser(available_blocks, string),
            string_of_blocks.split(' - '))))
        
        return unit


