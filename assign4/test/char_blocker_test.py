import unittest
from nose_parameterized import parameterized
from src.char_blocker import CharBlock

class CharBlockTest(unittest.TestCase):

    def setUp(self):
        self.test_block = CharBlock()

    @parameterized.expand([
            ['Z', 'Z', ''],
            ['Z', 'z', 'z'],
            ['Z', 'k', 'k'],
            ['z', '1', '1'],
            ['k', 'k', '']])
    def test_userdefined_process(self, userdefined_char_case, input_char, expected_char):
        self.test_block.case_setup(userdefined_char_case)
        self.assertEqual(self.test_block.process(input_char), expected_char)
