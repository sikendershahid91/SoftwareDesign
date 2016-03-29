def fibonacci_memoized(number):
    if number < 0:
        raise ValueError

    if number not in fibonacci_memoized.cache:
        fibonacci_memoized.cache[number] = (
            fibonacci_memoized(number - 2) + 
            fibonacci_memoized(number - 1))

    return fibonacci_memoized.cache[number]

fibonacci_memoized.cache = {0: 1, 1: 1}
