# Write a Python Program to Split the array and add the first part to the end?

def split_and_rotate_array(array):
    
    if not array:
        return array
    
    mid = len(array) // 2
    
    left_half = array[:mid]

    right_half = array[mid:]

    array[:] = [] #to modify existing array, instead of creating new
    
    array = right_half + left_half
    
    return array

array = [1,2,3,4,5,6,7]

print(f"Array before spliting and rotating : {array}")
result = split_and_rotate_array(array)


print(f"Array after spliting and rotating : {result}")