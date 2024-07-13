# Kyle Stewart CIS261 Lab: Iterative and Recursive Functionality
def factor(x):
    print("Factorial results using an iterative function")
    result = 1
    for i in range(1, x + 1):
        result *= i
        print(result)
    return result


def factor(x):
    print("Factorial results using a recurive function")
    if x == 0:
        return 1
    else:
        return n * factor2(n  -1)

