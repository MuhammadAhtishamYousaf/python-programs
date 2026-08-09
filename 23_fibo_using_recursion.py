# Write a Python Program to Display Fibonacci Sequence Using Recursion.

second_last = 0
last = 1

count = 2


def fibonacci(second_last, last, count):

    while count <= 10:
        new_fibo = second_last + last
        print(new_fibo)
        second_last = last
        last = new_fibo
        
        count += 1
        return fibonacci(second_last, last, count)


# print(second_last)
# print(last)
# fibonacci(second_last, last, count)


n_terms = 10
def fibo(n):
    if n <= 1:
        return n
    
    else:
        first = fibo(n-1)
        second = fibo(n - 2)
        new_fibo = first + second
        return new_fibo

for i in range(n_terms):
    print(fibo(i))