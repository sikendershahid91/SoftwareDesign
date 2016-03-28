def fibonacci_recursive(number):
    if number < 0:
        raise ValueError("Negative number!")

    return 1 if number < 2 else sum(map(
    	fibonacci_recursive, 
    	[number - 1, number - 2]))