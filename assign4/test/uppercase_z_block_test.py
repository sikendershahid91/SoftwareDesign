import unittest
from nose_parameterized import parameterized
from src.uppercase_z_block import ZBlock

class ZBlockTest(unittest.TestCase):

    def setUp(self):
        self.test_block = ZBlock()

    @parameterized.expand([
            ['A', 'A'],
            ['B', 'B'],
            ['a', 'a'],
            ['b', 'b'],
            ['1', '1'],
            ['Z', None]])
    def test_process(self, input_char, expected_char):
        self.assertEqual(self.test_block.process(input_char), expected_char)
