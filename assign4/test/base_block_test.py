import unittest
from src.base_block import BaseBlock


class BaseBlockTest(unittest.TestCase):


    def test_canary(self):
        self.assertTrue(self)


    def setUp(self):
        self.base_block = BaseBlock()
        

    def test_base_block_take_input_a_return_a(self):
        self.assertEqual(self.base_block.process('a'), 'a')

