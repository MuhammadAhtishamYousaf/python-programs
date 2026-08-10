# Write a Python Program to find sum of array.


array = [1,2,3,4,5]

# print(sum(array))

def sum_of_array(array):
    
    sum = 0
    for num in array:
        sum += num
    return sum

array_sum = sum_of_array(array)

print(array_sum)