# Write a Python program to print odd numbers in a List.

nums = [i for i in range(1, 40)]

odd_nums = [num for num in nums if num % 2 != 0]

print(odd_nums)