# ---------------------------------------------------------------
# Fibonacci and Factorial Calculator
# Author: Roxanne Prajapati
# Description:
#       Part 1: Generate a Fibonacci series and compute the factorial of a given number
#       Part 2: Use Math package to generate factorial of a given number
# ---------------------------------------------------------------

import math

def fibonacci_series(number):
    """
    Generate a Fibonacci series of length without using any packages.
    """
    series = []
    # Handle if number is 0 or 1
    if number <= 0:
        return series
    if number == 1:
        return [0]

    series = [0, 1]

    # Building the fibonacci series iteratively
    for _ in range(2, number):
        next_number = series[-1] + series[-2]
        series.append(next_number)

    return series


def factorial(number):
    """
    Compute factorial of a number without using any packages.
    """
    #Set the factorial result to 1 to handle the number if 0
    result = 1

    # Multiply 1 × 2 × ... × n
    for i in range(1, number + 1):
        result *= i

    return result

def main():
    """
    Main function that ask the User to enter the length Fibonacci series
    then display the Fibonacci series and its factorial
    """
    fibonacci_length = int(input("Enter the length of the Fibonacci series: "))

    print("The Fibonaci Series is:")
    print(fibonacci_series(fibonacci_length))
    print("The factorial of " + str(fibonacci_length) + " is " + str(factorial(fibonacci_length)))
    print("The factorial of " + str(fibonacci_length) + " using math package is " + str(math.factorial(fibonacci_length)))


# Run the program only when executed directly
if __name__ == "__main__":
    main()
