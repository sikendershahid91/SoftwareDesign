def fibonacci_recursive(number):
    if number < 0:
        raise ValueError

    return 1 if number in [0, 1] else (
    	fibonacci_recursive(number - 2) + fibonacci_recursive(number - 1))