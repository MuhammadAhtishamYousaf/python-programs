# Write a Python program to count the size of elements in list


array = [5,6,3,2,1,4]

print(len(array))

count = 0
for num in array:
    count += 1
    
print(f"Size of array : {count}")