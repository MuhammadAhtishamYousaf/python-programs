# Write a Python program to print even numbers in a list.

nums = [i for i in range(1,10)]

even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)