# Write a Python program to insertion at the beginning in OrderedDict.

from collections import OrderedDict


# Create an OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
# Item to insert at the beginning
new_item = ('a', 1)

new_ordered_dict = OrderedDict([new_item])

new_ordered_dict.update(ordered_dict)

print(new_ordered_dict)