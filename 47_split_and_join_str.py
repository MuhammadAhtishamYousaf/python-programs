# Write a Python program to split and join a string.


def split_and_join(input_str:str):
    list_of_words = input_str.split()
    print(f"List of String : {list_of_words}")
    
    separater = " "
    output_str = separater.join(list_of_words)
    return output_str

desc = "An even number is a number that can be divided by 2 with no remainder."
result = split_and_join(desc)
print(result)