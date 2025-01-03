#Recursividad

def recursive_func(n:int):
    print(n)
    if n > 0:
        recursive_func(n - 1)
        

recursive_func(100)

def factorial_func(n: int):
    if n == 0  or n == 1:
        return 1
    else:
        return (n * factorial_func(n-1))
    
print(factorial_func(5))

def fibonacci_func(n:int):
    if n == 1: 
        return 0
    elif n == 2:
        return 1
    else: 
        return fibonacci_func(n - 1) + fibonacci_func(n - 2)
    
print(fibonacci_func(7))