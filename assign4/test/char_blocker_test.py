import unittest
from nose_parameterized import parameterized
from src.char_blocker import CharBlock

class CharBlockTest(unittest.TestCase):


    @parameterized.expand([
            ['Z', 'Z', ''],
            ['Z', 'z', 'z'],
            ['Z', 'k', 'k'],
            ['z', '1', '1'],
            ['k', 'k', '']])
    def test_userdefined_process(self, defined_char_case, input_char, expected):
        self.test_block = CharBlock(defined_char_case)
        self.assertEqual(self.test_block.process(input_char), expected)
