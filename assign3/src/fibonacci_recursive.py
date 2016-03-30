class Recursive:
    
    def fibonacci(self, number):
        if number < 0:
            raise ValueError("Negative number!")

        return 1 if number < 2 else sum(
          map(self.fibonacci, [number - 1, number - 2]))
