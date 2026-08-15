# Write a Python program to Extract Unique dictionary values.

# Sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
    }

unique_values = set()
for value in my_dict.values():
    unique_values.add(value)

print(unique_values)