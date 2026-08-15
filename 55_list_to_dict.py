# Write a Python program to convert key-values list to flat dictionary.

key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

key_values_dict = dict(key_values_list)

print(key_values_dict)


# method 2 
flat_dict = {}
for key, value in key_values_list:
    flat_dict[key] = value 
    
print(flat_dict)