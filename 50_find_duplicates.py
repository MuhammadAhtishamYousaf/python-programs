# Write a Python program to find all duplicate characters in string.

# method 1
def find_duplicate_char(string: str):
    n = len(string)
    duplicates = []
    for i in range(n):
        for j in range(i + 1, n):
            if string[i] == string[j]:
                duplicates.append(string[i])
    
    return duplicates

# method 2 
def find_duplicates_with_dict(string: str):
    char_count = {}

    duplicates = []

    for i in string:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1
    
    for key, value in char_count.items():
        if value > 1:
            duplicates.append(key)
    return duplicates
            
string = "characters"
# string = "piyush sharma"

result = find_duplicates_with_dict(string)

print(result)