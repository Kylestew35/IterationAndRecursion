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

value = [0, 5, 10, 25, 50, 100]

print("Factorial results using an iterative function")
for u in value:
    result = factor_i(u)
    print(f"{u}! = {result}")


print("Factorial results using an recursive function")
for u in value:
    result = factor_r(u)
    print(f"{u}! = {result}")
