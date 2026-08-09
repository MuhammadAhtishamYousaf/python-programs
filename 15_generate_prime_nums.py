# Program 15 ¶ Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

lower = 1
upper = 10

for num in range(lower, upper + 1): #all prime nums are greater than 1
    if num > 1:
        for j in range(2, num): 
            if num % j == 0:
                break
        else:
            print(num)
            
# print(primes)