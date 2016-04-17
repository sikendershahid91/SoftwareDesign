import unittest
from nose_parameterized import parameterized
from src.userdefined_char_blocker_block import userdefinedCharBlock

class userdefinedCharBlockTest(unittest.TestCase):

    def setUp(self):
        self.test_block = userdefinedCharBlock()
                               
#Venkat: we need the following:
#toblock, input, expected
#'Z', 'Z', ""
#'Z', 'z', "z"
#'Z', 'k', "k"
#'Z', '1', "1"
#'k', 'k', ""

    @parameterized.expand([
            ['b', 'A', 'A'],
            ['b', 'b', '']])
    def test_userdefined_process(self, userdefined_char_case, input_char, expected_char):
        self.test_block.case_setup(userdefined_char_case)
        self.assertEqual(self.test_block.process(input_char), expected_char)
