# Write a Python Program to Print the Fibonacci sequence.

# prev2 = 0
# prev1 = 1

# fibos = [prev2, prev1]
# for num in range(10):
#     new_fibo = prev2 + prev1
#     prev2 = prev1
#     prev1 = new_fibo
#     fibos.append(new_fibo)

# print(fibos)

n = 15
count = 0

n2, n1 = 0, 1
print(n2) 
print(n1) 
while count <= n:
    new_fibo = n2 + n1
    
    n2 = n1
    n1 = new_fibo
    
    print(new_fibo)
    count += 1
