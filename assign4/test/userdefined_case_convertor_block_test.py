import unittest
from nose_parameterized import parameterized
from src.userdefined_case_convertor_block import userdefinedCaseConvertorBlock


class userDefinedCaseConvertorTest(unittest.TestCase): #Venkat: Remove

    @parameterized.expand([
            ['b', 'A', 'A'],
            ['b', 'b', 'B']])
    def test_userdefined_process(self, userdefined_char_case, input_char, expected_char):
        self.test_block = userdefinedCaseConvertorBlock()
        self.test_block.case_setup(userdefined_char_case)
        self.assertEqual(self.test_block.process(input_char), expected_char)
