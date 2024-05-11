import grpc

def sum_up_to(i):
    result = 0
    for val in range(i+1):
        result = result + val
    return result

def factorial(j):
    result = 1
    for val in range(1, j+1):
        result = result * val
    return result

print(sum_up_to(5))
print(factorial(5))
