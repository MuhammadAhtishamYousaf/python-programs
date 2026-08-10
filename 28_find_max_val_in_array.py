# Write a Python Program to find largest element in an array.


array = [1,2,3,4,5]

# print(max(array))

def find_max_value(array: list):
    if not array:
        return array
    
    largest_value = array[0]

    for num in array:
        if num > largest_value:
            largest_value = num
    
    return largest_value


max_val = find_max_value(array)

print(max_val)