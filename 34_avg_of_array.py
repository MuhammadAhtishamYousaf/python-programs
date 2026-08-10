# Write a Python program to find avg of elements in list.

array = [1,2,3,4,7,10,11]

def find_avg(array):

    array_sum = 0
    array_count = 0
    for num in array:
        array_sum += num
        array_count += 1
        
    array_avg = array_sum / array_count
    
    return round(array_avg, 2)

avg = find_avg(array)

print(avg)