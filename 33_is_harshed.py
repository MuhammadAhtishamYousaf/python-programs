# Write a Python program to determine whether the given number is a Harshad
# Number.

num = 19

def is_harshad(num):
    digit_sum = sum(int(digit) for digit in str(num))
    
    return num % digit_sum == 0
    
result = is_harshad(num)

print(result)


# t = (1,2,3,4)
# print(sum(t))
# print(max(t))
# print(min(t))
# print(len(t))