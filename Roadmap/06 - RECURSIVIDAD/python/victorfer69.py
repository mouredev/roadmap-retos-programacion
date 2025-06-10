#FUNCION RECURSIVA DEL 0 AL 100

def recursive_function(n:int):
    if n == 100:
        print(n)
    else:
        print(n)
        recursive_function(n+1)
    
recursive_function(0)


#EJERCICIO EXTRA
def factorial(n:int):
    if n > 0:
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    else:
        print("Numero invalido")
        return 0

print(factorial(5))


def fibonacci(n:int):
    if n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    else:
        print("Numero invalido")
        return 0
    
print(fibonacci(10))