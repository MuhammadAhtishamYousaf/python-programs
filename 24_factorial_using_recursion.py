# Write a Python Program to Find Factorial of Number Using Recursion.


def factorial(n):
    if n == 0:
        return 1
    
    fact = n * factorial(n-1)
    return fact


print(factorial(3))