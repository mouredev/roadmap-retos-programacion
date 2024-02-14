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

"""
""" def fibonacci(n_fib :  int, fib1=0, fib2=1):
    if n_fib == 0:
        return fib1
    elif n_fib == 1:
        return fib2
    else:
        return n_fibonacci(n_fib - 1, fib2, fib1 + fib2) """

#print(n_fibonacci(4))
def n_fibonacci(n_fib :  int, fib1=0):
    if n_fib == 0:
        return fib1
    elif n_fib == 1:
        return fib1 + 1
    else:
        return fib1 + n_fibonacci(n_fib - 1,  fib1 + fib1 - 1)