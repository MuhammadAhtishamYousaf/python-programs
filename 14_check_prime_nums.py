# Program 14: Write a Python Program to Check Prime Number.


num = 2

prime = True

if num < 2:
    print(f"{num} is not a prime number")
    
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
            
    if prime:
        print(f"{num} is prime")
            
    else:
        print(f"{num} is not a prime number")
        