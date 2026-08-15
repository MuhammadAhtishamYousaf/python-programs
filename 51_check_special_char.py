# Write a Python Program to check if a string contains any special character.

import re
def is_special(input_str: str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    
    if re.search(pattern,input_str):
        return True
    
    else:
        return False 

# input_str = "ahtishamgmailcom"
input_str = "ahtisham@gmail.com"

result = is_special(input_str)

print(result)