import unittest
from src.fibonacci_memoized_recursive import fibo_memoized_recur


class FibonacciTest(unittest.TestCase):


    def test_canary(self):
        self.assertTrue(self)


    def test_negative_position_throws_exception(self):
        self.assertRaises(ValueError, fibo_memoized_recur, -1)


    def test_position_0_return_1(self):
        self.assertEqual(1, fibo_memoized_recur(0))


    def test_position_1_return_1(self):
        self.assertEqual(1, fibo_memoized_recur(1))


    def test_position_2_return_2(self):
        self.assertEqual(2, fibo_memoized_recur(2))


    def test_position_4_return_5(self):
        self.assertEqual(5, fibo_memoized_recur(4))


    def test_position_3_return_3(self):
        self.assertEqual(3, fibo_memoized_recur(3))


    def test_position_5_return_8(self):
        self.assertEqual(8, fibo_memoized_recur(5))


    def test_position_6_return_13(self):
        self.assertEqual(13, fibo_memoized_recur(6))        