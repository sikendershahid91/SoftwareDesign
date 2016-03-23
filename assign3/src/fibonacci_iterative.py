def fibonacci_iterative(number):
    if number < 0:
        raise ValueError("Negative number!")

    if number == 0 or number == 1:
        return 1
        
    number_before_1 = 1
    number_before_2 = 1
    fibo_result = 1
    for i in range(number - 1):
      fibo_result = number_before_1 + number_before_2
      number_before_2 = number_before_1
      number_before_1 = fibo_result

    return fibo_result
