# ---------------------------------------------------------------
# Fibonacci and Factorial Calculator Class
# Author: Roxanne Prajapati
# Description:
#      Converting the previous activities into Class and Object
# ---------------------------------------------------------------
import math


class Calculator:

    def get_factorial(self, number):
        if number == 0:
            return 1
        return math.factorial(number)

    def get_fibonacci(self, number):
        if number <= 1:
            return number

        return self.get_fibonacci(number -1) + self.get_fibonacci(number-2)

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")
    n = int(input("Enter a number: "))
    calculator = Calculator()

    if choice == "1":
        ans = calculator.get_factorial(n)
    elif choice == "2":
        ans = calculator.get_fibonacci(n)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)