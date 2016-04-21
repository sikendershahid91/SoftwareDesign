import unittest
from functools import reduce
from nose_parameterized import parameterized
from src.processing_unit import ProcessingUnit
from src.multiplier_block import MultiplierBlock
from src.lowercase_converter_block import LowerCaseConverterBlock
from src.uppercase_converter_block import UpperCaseConverterBlock
from src.char_blocker import CharBlock


class ProcessingUnitTest(unittest.TestCase):


    def setUp(self):
        self.present_blocks = [LowerCaseConverterBlock, 
           UpperCaseConverterBlock, MultiplierBlock, CharBlock]


    @parameterized.expand([
            [[UpperCaseConverterBlock(), CharBlock('Z')], 
               'abczz', 
               'ABC'],
            [[MultiplierBlock(), CharBlock('a')], 
               'abczz', 
               'bbcczzzz'],
            [[CharBlock('Z'), LowerCaseConverterBlock()], 
               'abCZz', 
               'abcz'],])
    def test_unit_process(self, list_of_blocks, input_string, expected_output):
    	self.processing_unit = ProcessingUnit(list_of_blocks)
    	self.assertEqual(expected_output, 
    		self.processing_unit.process(input_string))