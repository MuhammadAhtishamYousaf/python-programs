# Write a Python program to find second largest number in a list.


array = [0,6,3,2,1,4,10]

# array.sort()
# print(array[-2])

largest = array[0]
second_largest = array[0]
for num in array[1:]:
    if num > largest:
        second_largest = largest
        largest = num 
        
print(largest)
print(second_largest)
        
    