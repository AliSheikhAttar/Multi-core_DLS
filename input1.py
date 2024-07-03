import math
# Function definition
def compute_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")

numbers = [5, 7, 10, 12, 15, 18, 20, 25, 30, 35]
for number in numbers:
       compute_factorial(number)