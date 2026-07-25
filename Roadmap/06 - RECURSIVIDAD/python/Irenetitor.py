#Recursive

def countdown(num: int):
    if num >= 0:
        print(num)
        countdown(num - 1)

countdown(100)

#Extra Exercise

#Factorial

def factorial(numb:int):
    if numb < 0:
        print(f"The number must be positive")
    elif numb == 1 or numb == 0:
        return 1
    else:
        return numb * factorial(numb - 1)

print(factorial(34))

#Fibonacci

def fibonacci(n):
    if n < 0:
        print("Please enter a non-negative number")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))
