import unittest
from nose_parameterized import parameterized
from src.uppercase_converter_block import UpperCaseConverterBlock


class UpperCaseConverterBlockTest(unittest.TestCase):


    def setUp(self):
        self.test_block = UpperCaseConverterBlock()


    @parameterized.expand([
            ['A', 'A'],
            ['B', 'B'],
            ['a', 'A'],
            ['b', 'B'],
            ['1', '1'],
            ['#', '#']])
    def test_process(self, input_char, expected_char):
        self.assertEqual(self.test_block.process(input_char), expected_char)
