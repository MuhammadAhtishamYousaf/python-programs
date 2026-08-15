# Write a Python program for removing i-th character from a string.

string = 'Hello, wWorld'

def remove_char(string: str, i):
    if i < 0 and i > len(string):
        print(f"Invalid index {i}. The string remains unchanged.")
        return string
    
    clean_string = string[:i] + string[i+1:]
    
    return clean_string

result = remove_char(string, 7)

print(result)