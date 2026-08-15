# Write a Python program to find the sum of all items in a dictionary.


# Sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
    }

sum = 0
for value in my_dict.values():
    sum += value
    
print(sum)
