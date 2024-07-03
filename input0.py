import math
def compute_factorial(start, end):
    for i in range(start, end):
        result = math.factorial(i)
        print(f"Factorial of {i} is {result}")


compute_factorial(1, 10)