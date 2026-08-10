# Write a Python Program to check if given array is Monotonic.

# A monotonic array is one that is entirely non-increasing or non-decreasing.


array1 = [1,2,3]
array2 = [1,2,4,3]

def check_is_monotonic(array: list):
    
    if len(array) <= 2 : 
        return True 
    
    direction = "unknown"
    
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            if direction == 'decreasing':
                return False
            
            direction = 'increasing'
            
        elif array[i] > array[i + 1]:
            if direction == 'increasing':
                return False 
            
            direction = 'decreasing' 

        else:
            continue
            
    return True

# is_monotonic = check_is_monotonic(array1)

# print(is_monotonic)

def is_monotonic(array):
    
    increasing = decreasing = True
    
    for i in range(1, len(array)):
        
        current = array[i]
        prev = array[i-1]
        if current > prev:
            decreasing = False 
        
        elif current < prev:
            increasing = False 
        
            
    return increasing or decreasing

result = is_monotonic(array2)
print(result)