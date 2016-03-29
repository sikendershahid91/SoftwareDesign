from functools import reduce

def fibonacci_iterative(number):
    if number < 0:
        raise ValueError("Negative number!")

    return reduce(
        lambda previous, index: [previous[1], sum(previous)],
        range(number + 1), [1, 0]) [1]
