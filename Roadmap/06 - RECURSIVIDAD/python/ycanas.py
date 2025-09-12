# I. Ejercicio

def my_func(n):
    if n < 0:
        return
    
    print(n)
    my_func(n - 1)


print()
print(" Ejercicio ".center(30, '-'), end="\n\n")
my_func(100)


# II. Extra

def factorial(n):
    if n <= 2:
        return n
    
    return factorial(n - 1) * n


def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


print()
print(" Factorial ".center(30, '-'), end="\n\n")
print(factorial(5))

print()
print(" Fibonacci ".center(30, '-'))
print(fibonacci(8))
