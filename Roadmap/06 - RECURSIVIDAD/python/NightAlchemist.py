# print from 100 to 0

def cowntown(number):
    if number >= 0:
        print(number)
        number = cowntown(number - 1)

cowntown(100)

#factorial

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
number_fact = int(input("Number to factor:"))
factorial_result = print(f"The factorial result is: {factorial(number_fact)}")

#fibonacci

def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number_fib = int(input("Fibonacci position number:"))
print(f"The value in this position of the Fibonacci series is: {fibonacci(number_fib)}")