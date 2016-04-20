import unittest
from nose_parameterized import parameterized
from src.multiplier_block import MultiplierBlock

class MultiplierBlockTest(unittest.TestCase):

    def setUp(self):
        self.test_block = MultiplierBlock()

    @parameterized.expand([
            ['A', 'AA'],
            ['B', 'BB'],
            ['a', 'aa'],
            ['b', 'bb'],
            ['1', '11'],
            ['#', '##']])
    def test_process(self, input_char, expected_char):
        self.assertEqual(self.test_block.process(input_char), expected_char)


    @parameterized.expand([
            ['Multiplier', MultiplierBlock],
            ['multiplier', None],
            ['aabc', None]])
    def test_handle_string(self, string, expected_answer):
        answer = self.test_block.handle_string(string)
        self.assertTrue(answer == expected_answer 
            or isinstance(answer, expected_answer))
