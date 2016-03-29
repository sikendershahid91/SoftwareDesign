import unittest
from src.fibonacci_memoized import fibonacci_memoized
from test.fibonacci_test import fibonacciTest


class FibonacciMemoizedTest(unittest.TestCase, fibonacciTest):
    def setUp(self):
        self.fibonacci = fibonacci_memoized
