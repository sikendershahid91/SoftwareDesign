
import unittest
from src.fibonacci_recursive import Recursive
from src.fibonacci_memoized import Memoized
from timeit import timeit

class FibonacciPerformanceTest(unittest.TestCase):

    def test_recursive_10_times_slower_than_memoized_with_number_25(self):
        memoized_time = timeit("Memoized().fibonacci(25)", 
            setup = "from fibonacci_memoized import Memoized", 
            number = 1)

        recursive_time = timeit("Recursive().fibonacci(25)", 
            setup = "from fibonacci_recursive import Recursive", 
            number = 1)

        self.assertTrue(recursive_time > 10 * memoized_time)
