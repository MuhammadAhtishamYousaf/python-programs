# Write a Python program to find uncommon words from two Strings.

def find_uncommon_words(str1:str, str2: str):
    words1 = set(str1.split())
    words2 = set(str2.split())
    
    return list(words1.symmetric_difference(words2))

# Input two strings
string1 = "This is the first string"
string2 = "This is the second string"

result = find_uncommon_words(string1, string2)

print(result)