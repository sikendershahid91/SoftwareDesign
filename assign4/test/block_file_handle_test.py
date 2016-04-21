import unittest
from nose_parameterized import parameterized
from unittest.mock import mock_open, patch
import builtins

from src.multiplier_block import MultiplierBlock
from src.lowercase_converter_block import LowerCaseConverterBlock
from src.uppercase_converter_block import UpperCaseConverterBlock
from src.char_blocker import CharBlock

from src.block_file_handle import block_file_handle


class BlockFileHandleTest(unittest.TestCase):


    def test_block_file_handle(self):
        mock_lines = [
            'multiplier_block MultiplierBlock',
            'lowercase_converter_block LowerCaseConverterBlock',
            'uppercase_converter_block UpperCaseConverterBlock',
            'char_blocker CharBlock z']

        expected_blocks = [
            MultiplierBlock(),
            LowerCaseConverterBlock(),
            UpperCaseConverterBlock(),
            CharBlock('z')]

        test_chars = ['a', 'b', 'y', 'Y', 'z', 'Z', '#']

        mock_file = mock_open(read_data = '\n'.join(mock_lines))
        with patch('builtins.open', mock_file):
            created_blocks = block_file_handle('mock.txt')

        block_behavior_same = lambda expected, created: (
            False not in map(lambda char: 
                expected.process(char) == created.process(char), test_chars))

        self.assertTrue(False not in 
            map(block_behavior_same, expected_blocks, created_blocks))