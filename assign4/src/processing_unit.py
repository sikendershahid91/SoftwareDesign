from functools import reduce
from src.multiplier_block import MultiplierBlock
from src.lowercase_converter_block import LowerCaseConverterBlock
from src.uppercase_converter_block import UpperCaseConverterBlock
from src.char_blocker import CharBlock

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
    def string_to_block_parser(cls, string):
        splited_string = string.split('-')
        if string == 'UpperCaseConverter':
            return UpperCaseConverterBlock()
        elif string == 'LowerCaseConverter':
            return LowerCaseConverterBlock()
        elif string == 'Multiplier':
            return MultiplierBlock()
        elif len(splited_string) == 2 and splited_string[1] == 'blocker':
            return  CharBlock(string.split('-')[0])
        raise ValueError('Unable to parse block type from {}'.format(string))


    @classmethod
    def from_string_factory(cls, string_of_blocks):
        unit = cls(list(map(
            cls.string_to_block_parser,
            string_of_blocks.split(' - '))))
        
        return unit


