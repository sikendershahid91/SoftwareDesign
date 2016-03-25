from functools import reduce

def fibonacci_iterative(number):
    if number < 0:
        raise ValueError("Negative number!")

    return reduce(
        lambda fibo_nums, iteration: [fibo_nums[1], fibo_nums[0] + fibo_nums[1]],
        range(number), [1, 1]) [0]
