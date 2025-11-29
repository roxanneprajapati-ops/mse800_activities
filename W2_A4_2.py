# ---------------------------------------------------------------
# TITLE HERE
# Author: Your Name
# Description:
#      
# ---------------------------------------------------------------

class MathSeries:
    # @staticmethod
    def factorial_recursive(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * self.factorial_recursive(n - 1)



    # @staticmethod
    def fibonacci_recursive(self,n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def fibonacci_series(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        series = self.fibonacci_series(n - 1)
        series.append(series[-1] + series[-2])
        return series


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    math_series = MathSeries()
    print("Factorial (recursive):", math_series.factorial_recursive(n))
    print("Fibonacci (recursive):", math_series.fibonacci_series(n))


