# Write a Python program to check if a given string is binary string or not.

def is_binary(input_str: str):
    for char in input_str:
        if char not in '01': # Check if the i is not '0' or '1'
            return False
    return True 


# input_str = "numbers"
input_str = "1001110"

result = is_binary(input_str)
print(result)
print(f"'{input_str}' is {"not" if not result else ""} binary.")