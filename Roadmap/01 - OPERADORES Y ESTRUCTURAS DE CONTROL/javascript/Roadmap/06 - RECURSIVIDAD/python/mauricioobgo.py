"""
Entendiendo el concepto

"""
def count_down(number : int):
    if number < 0 :
        return
    print(number,sep='')
    count_down(number-1)

#count_down(10)

"""
Factorial Calculation

"""
def factorial(number: int, fact=1) -> int:
    if number <= 1:
        return fact
    return factorial(number - 1, fact * number)

#print(factorial(3))

"""
Nth Fibonacci number
"""
def fibonacci(n_fib :  int, fib1=0, fib2=1):
    if n_fib == 0:
        return fib1
    elif n_fib == 1:
        return fib2
    else:
        return fibonacci(n_fib - 1, fib2, fib1 + fib2)
