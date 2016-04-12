import unittest
from src.lowercase_converter_block import LowerCaseConverterBlock


class LowerCaseConverterBlockTest(unittest.TestCase):


    def test_canary(self):
        self.assertTrue(self)


    def setUp(self):
        self.test_block = LowerCaseConverterBlock()
        

    def test_process(self):
        expected_returns = {
            'A': 'a',
            'B': 'b',
            'a': 'a',
            'b': 'b',
            '1': '1'
        }
        for input_char, expected_char in expected_returns.items():
            self.assertEqual(self.test_block.process(input_char), 
                expected_char)

