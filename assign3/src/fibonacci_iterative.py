from functools import reduce

def fibonacci_iterative(number):
    if number < 0:
        raise ValueError("Negative number!")

    return reduce(
        lambda previous, index: [previous[1], sum(previous)],
          range(number + 1), [1, 0]) [1]  #Venkat: I have added indentation to show this is part of the expression from the previous line. If l and r on the same veritcal indentation, that means they are two different expressions, but they are not. So indented r further.
        
