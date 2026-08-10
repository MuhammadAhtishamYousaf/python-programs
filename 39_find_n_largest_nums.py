# Write a Python program to find N largest elements from a list.

array = [5, 6, 3, 2, 1, 4]

def find_n_large_elements(array, n):
    sorted_array = sorted(array)
    top_n_values = sorted_array[n:]
    return top_n_values

result = find_n_large_elements(array, 3)
print(result)