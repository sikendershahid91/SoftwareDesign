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


    @parameterized.expand([
            ['Z-blocker', (CharBlock, 'Z')],
        	['z-blocker', (CharBlock, 'z')],
            ['a--blacker', None]])
    def test_handle_string(self, string, expected):
        answer = CharBlock.handle_string(string)
        self.assertTrue(
        	(answer == expected) or
            (isinstance(answer, expected[0]) and answer._char == expected[1]))
