def printNums (num) :
    if num < 0:
        return
    print(num)

    printNums(num - 1)

printNums(100)

"""
EXTRA
"""
def factorial(n):
    if n == 0 or n == 1:
        result = 1
    elif n > 1:
        result = n * factorial (n - 1)
    return result

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)

for n in range(10):
    print(fibonacci(n))
    

