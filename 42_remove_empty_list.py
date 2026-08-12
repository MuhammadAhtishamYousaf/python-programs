# Write a Python program to Remove empty List from List.

list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

# if want to use same list 

# for list in list_of_lists:
#     if not list:
#         list_of_lists.remove(list)

# print(list_of_lists)

clean_list = [list for list in list_of_lists if list]

print(clean_list)