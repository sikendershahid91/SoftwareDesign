import unittest
from nose_parameterized import parameterized
from src.lowercase_z_block import zBlock


class zBlockTest(unittest.TestCase):

    def setUp(self):
        self.test_block = zBlock()

    @parameterized.expand([
            ['A', 'A'],
            ['B', 'B'],
            ['a', 'a'],
            ['b', 'b'],
            ['1', '1'],
            ['z', None]])
    def test_process(self, input_char, expected_char):
        self.assertEqual(self.test_block.process(input_char), expected_char)
