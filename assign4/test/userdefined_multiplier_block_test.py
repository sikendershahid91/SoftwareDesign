import unittest
from nose_parameterized import parameterized
from src.userdefined_multiplier_block import userdefinedMultiplierBlock

class userdefinedMultiplierBlockTest(unittest.TestCase):

    def setUp(self):
        self.test_block = userdefinedMultiplierBlock()

    @parameterized.expand([
            ['1', 'A', 'A'],
            ['2', 'B', 'BB'],
            ['3', 'a', 'aaa'],
            ['4', 'b', 'bbbb'],
            ['5', '1', '11111'],
            ['2', '#', '##']])
    def test_process(self, input_factor, input_char, expected_char):
        self.test_block.factor_setup(input_factor)
        self.assertEqual(self.test_block.process(input_char), expected_char)
