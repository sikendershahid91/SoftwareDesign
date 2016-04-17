import unittest
from nose_parameterized import parameterized
from src.lowercase_k_block import kBlock

class kBlockTest(unittest.TestCase):   #Venkat: Remove

	@parameterized.expand([
		['b', 'b'],
        ['1', '1'],
        ['#', '#'],
		['k', '']])
	def test_process(self, input_char, expected_char):
		self.test_block = kBlock()
		self.assertEqual(self.test_block.process(input_char), expected_char)
