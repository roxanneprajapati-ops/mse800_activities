# ---------------------------------------------------------------
# Fibonacci and Factorial Calculator Class
# Author: Roxanne Prajapati
# Description:
#      Converting the previous activities into Class and Object
# ---------------------------------------------------------------
import math


class Calculator:
    def __init__(self, choice, number):
        self.choice = choice
        self.number = number

    def get_factorial(self):
        if self.number == 0:
            return 1
        return math.factorial(self.number)

    def fibonacci(self):
        if self.number <= 1:
            return self.number

        return self.number -1 + self.number - 2

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")
    n = int(input("Enter a number: "))
    calculator = Calculator(choice, n)

    if choice == "1":
        ans = Calculator.get_factorial
    elif choice == "2":
        ans = Calculator.fibonacci
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)