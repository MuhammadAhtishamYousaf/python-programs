# Write a Python Program to Sort Words in Alphabetic Order.


words_str = input("Enter words... ")
words_array = [word.capitalize() for word in words_str.split()]
# array.sort() #it sort and retutn None
sorted_array = sorted(words_array) # it not only sort but also return sorted list

print(sorted_array)