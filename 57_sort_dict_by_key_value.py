# Write a Python program to sort Python Dictionaries by Key or Value.

#sort by keys
sample_dict = {'mango': 5,'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_dict_by_keys = dict(sorted(sample_dict.items()))

print(sorted_dict_by_keys)

#sort by values
sorted_dict_by_values  = dict(sorted(sample_dict.items(), key = lambda item: item[1]))

print(sorted_dict_by_values)