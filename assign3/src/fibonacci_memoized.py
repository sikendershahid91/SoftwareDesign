from fibonacci_recursive import Recursive

class Memoized(Recursive):

    def __init__(self):
        self._cache = {}
    
    def fibonacci(self, number):
        if number not in self._cache:
            self._cache[number] = super().fibonacci(number)
        return self._cache[number]
