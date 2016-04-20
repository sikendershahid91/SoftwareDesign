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


    @parameterized.expand([
        ['UpperCaseConverter', UpperCaseConverterBlock],
        ['LowerCaseConverter', LowerCaseConverterBlock],
        ['Multiplier', MultiplierBlock]])
    def test_block_parser_without_char_blocker(self, string, block_type):
        self.assertTrue(isinstance(
            ProcessingUnit.block_parser(self.present_blocks, string),
            block_type))


    @parameterized.expand([
        ['Z-blocker', 'Z'],
        ['z-blocker', 'z'],
        ['k-blocker', 'k']])
    def test_block_parser_with_char_block(self, string, blocked_char):
        output_block = ProcessingUnit.block_parser(self.present_blocks, string)
        self.assertTrue(isinstance(output_block, CharBlock) and 
            output_block._char == blocked_char)


    @parameterized.expand([
        'Multiplicity',
        'z_blocker',
        'lowercaseConverter'])
    def test_string_to_block_parser_raises_value_error(self, string):
        self.assertRaises(ValueError, 
            ProcessingUnit.block_parser, self.present_blocks, string)


    def test_from_string_factory(self):
        processing_unit = ProcessingUnit.from_string_factory(
            self.present_blocks,
            'UpperCaseConverter - Z-blocker - LowerCaseConverter')

        expected_block_type_sequence = [UpperCaseConverterBlock, CharBlock, 
            LowerCaseConverterBlock]

        self.assertTrue(map(
            isinstance, 
            processing_unit._blocks, 
            expected_block_type_sequence))