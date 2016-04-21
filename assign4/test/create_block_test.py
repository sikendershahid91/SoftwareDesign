import unittest
from nose_parameterized import parameterized
from src.processing_unit import ProcessingUnit
from src.multiplier_block import MultiplierBlock
from src.lowercase_converter_block import LowerCaseConverterBlock
from src.uppercase_converter_block import UpperCaseConverterBlock
from src.char_blocker import CharBlock

from src.create_block import create_block


class BlockCreateTest(unittest.TestCase):

    @parameterized.expand([
        ['multiplier_block MultiplierBlock',
            MultiplierBlock()],
        ['lowercase_converter_block LowerCaseConverterBlock',
            LowerCaseConverterBlock()],
        ['uppercase_converter_block UpperCaseConverterBlock',
            UpperCaseConverterBlock()],
        ['char_blocker CharBlock z', CharBlock('z')],
        ['char_blocker CharBlock Z', CharBlock('Z')],
        ['char_blocker CharBlock a', CharBlock('a')] ])
    def test_created_block_successful_same_behavior(self, string, expected):
        chars = ['a', 'b', 'y', 'Y', 'Z', '#']
        created = create_block(string)
        self.assertTrue(False not in
            [expected.process(char) == created.process(char) for char in chars])
