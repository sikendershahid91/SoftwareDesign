import unittest
from nose_parameterized import parameterized
from src.uppercase_z_block import ZBlock
from src.lowercase_z_block import zBlock

class zBlockTest(unittest.TestCase):

    @parameterized.expand([
    		['A', 'A'],
    		['b', 'b'],
            ['1', '1'],
            ['#', '#'],
            ['Z', '']])
    def test_process(self, input_char, expected_char):
        self.test_block = ZBlock()
        self.assertEqual(self.test_block.process(input_char), expected_char)

    @parameterized.expand([
    		['b', 'b'],
            ['1', '1'],
            ['#', '#'],
            ['z', '']])
    def test_process(self, input_char, expected_char):
        self.test_block = zBlock()
        self.assertEqual(self.test_block.process(input_char), expected_char)
