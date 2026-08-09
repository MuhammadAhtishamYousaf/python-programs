# Program 2: Write a Python program to do arithmetical operations addition and division.

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
operation = input("Enter operation +, -, /, * : ").strip().lower()

operations = [
    "+", "-", "*", "/", 
    "div", "division", "divide", "plus", 
    "add", "addition", "minus", "subtraction", 
    "mul", "multiplication", "multiply"
    ]

result = None

if operation in operations:
    if operation in ['+', "addition", "plus", "add"]:
        result = num1 + num2
    
    elif operation in ["-", "subtract", "minus", "subtraction"]:
        result = num1 - num2
    
    elif operation in ["/", "div", "divide" "division"]:
        result = None if num2 == 0 else num1 / num2 
    
    elif operation in ["*", "mul", "multiply", "multiplication"]:
        result = num1 * num2
        
    if result is None and num2 == 0:
        print(f"Zero Division Error")
        
    print(f"{operation} of {(num1)} & {num2} is {result}")
    
    
    
else:
    # print("Operation {} is not allowd!".format(operation)) #same
    # print("Operation {operation} is not allowd!".format(operation = operation)) #same
    print(f"Operation {operation} is not allowd!") #same but modern