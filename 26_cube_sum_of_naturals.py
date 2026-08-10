# Write a Python Program for cube sum of first n natural numbers?


def cube_sum(n: int):
    
    # for num in range(1, n):
    #     sum = num ** 3
    #     print(sum)
    
    sum = [i ** 3 for i in range(1, n+1)]
    return sum
        
print(cube_sum(4))