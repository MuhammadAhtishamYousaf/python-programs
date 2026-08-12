# Write a Python program to Count occurrences of an element in a list.

nums = [3,4,5,6,4,3]

def find_occurance(nums: list, element):
    # count = nums.count(element)
    
    count = 0
    for num in nums:
        if num == element:
            count += 1
    return count

element = 5
count = find_occurance(nums, element)
print(f"The element {element} appears {count} times in the list.")