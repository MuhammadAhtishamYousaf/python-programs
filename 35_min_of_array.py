# Write a Python program to find lowest of elements in list


array = [1,2,3,4,0]
t = (5,3,2,6,0)
s = {5,3,2,6,0,1,4}
print(s)
print(min(s))

# min_val = array[0]
# min_val = t[0]
# min_val = s[0] #not allowd in set
min_val = 0
for num in s:
    if num < min_val:
        min_val = num
        
print(min_val)






