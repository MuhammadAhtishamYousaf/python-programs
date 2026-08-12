# Write a Python program to Cloning or Copying a list.

# 1. Using Using the Slice Operator
original_list = [1, 2, 3, 4, 5]

# new_list = original_list.copy()
# new_list = original_list[:]
# new_list = original_list[::]
# new_list = original_list[0::]
new_list = original_list[0:]

print(new_list)

# 2. Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)