import unittest
from nose_parameterized import parameterized
from src.processing_unit import ProcessingUnit
from src.multiplier_block import MultiplierBlock
from src.lowercase_converter_block import LowerCaseConverterBlock
from src.uppercase_converter_block import UpperCaseConverterBlock
from src.char_blocker import CharBlock


class ProcessingUnitTest(unittest.TestCase):

    def setUp(self):
        self.processing_unit = ProcessingUnit()

    @parameterized.expand([
            [[UpperCaseConverterBlock(), CharBlock(char = 'Z')], 
               'abczz', 
               'ABC'],
            [[MultiplierBlock(), CharBlock(char = 'a')], 
               'abczz', 
               'bbcczzzz'],
            [[CharBlock(char = 'Z'), LowerCaseConverterBlock()], 
               'abCZz', 
               'abcz'],])
    def test_unit_process(self, list_of_blocks, input_string, expected_output):
    	self.processing_unit.set_blocks(list_of_blocks)
    	self.assertEqual(expected_output, 
    		self.processing_unit.process(input_string))
