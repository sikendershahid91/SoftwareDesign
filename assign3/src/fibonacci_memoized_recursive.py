def fibo_memoized_recur(number):
    if number < 0:
        raise ValueError

    if number not in fibo_memoized_recur.cache:
        fibo_memoized_recur.cache[number] = (
            fibo_memoized_recur(number - 2) + 
            fibo_memoized_recur(number - 1))
 
    return fibo_memoized_recur.cache[number]

fibo_memoized_recur.cache = {0: 1, 1: 1}