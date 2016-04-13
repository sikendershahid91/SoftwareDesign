import unittest
from nose_parameterized import parameterized
from src.lowercase_converter_block import LowerCaseConverterBlock


class LowerCaseConverterBlockTest(unittest.TestCase):


    def test_canary(self):
        self.assertTrue(self)


    def setUp(self):
        self.test_block = LowerCaseConverterBlock()


    @parameterized.expand([
            ['A', 'a'],
            ['B', 'b'],
            ['a', 'a'],
            ['b', 'b'],
            ['1', '1'],
            ['#', '#']])
    def test_process(self, input_char, expected_char):
        self.assertEqual(self.test_block.process(input_char), expected_char)

