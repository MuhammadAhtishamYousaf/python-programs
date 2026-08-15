# Write a Python program to Merging two Dictionaries.


dict1 = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}
dict2 = {
    'e': 10,
    'f': 20,
    'g': 10,
    'h': 30,
    'i': 20
}

# method 1
dict1.update(dict2)
print(dict1)

merge_dicts = {**dict1, **dict2}
print(merge_dicts)