# Kyle Stewart CIS261 Lab: Iterative and Recursive Functionality
def factor_i(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def factor_r(x):
    if x == 0:
        return 1
    else:
        return x * factor_r(x - 1)

print("Factorial results using an iterative function")
u = 0
result = factor_i(u)
print(f"{u}! = {result}")
u = 5
result = factor_i(u)
print(f"{u}! = {result}")
u = 10
result = factor_i(u)
print(f"{u}! = {result}")
u = 25
result = factor_i(u)
print(f"{u}! = {result}")
u = 50
result = factor_i(u)
print(f"{u}! = {result}")
u = 100
result = factor_i(u)
print(f"{u}! = {result}")

print("Factorial results using an recursive function")
u = 0
result = factor_r(u)
print(f"{u}! = {result}")
u = 5
result = factor_r(u)
print(f"{u}! = {result}")
u = 10
result = factor_r(u)
print(f"{u}! = {result}")
u = 25
result = factor_r(u)
print(f"{u}! = {result}")
u = 50
result = factor_r(u)
print(f"{u}! = {result}")
u = 100
result = factor_r(u)
print(f"{u}! = {result}")
