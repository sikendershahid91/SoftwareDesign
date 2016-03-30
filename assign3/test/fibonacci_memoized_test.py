import unittest
from src.fibonacci_memoized import Memoized
from test.fibonacci_test import fibonacciTest


class FibonacciMemoizedTest(unittest.TestCase, fibonacciTest):
    def setUp(self):
        self.memoized = Memoized()
        self.fibonacci = self.memoized.fibonacci
