#06git 
def regresiva(n):
    if n == 0:  # caso base
        print(n)
    else:
        print(n)
        regresiva(n - 1) # llamada recursiva
        
regresiva(100)

# Ejercicio extra 1
def factorial(n):
    if n == 1:  # caso base
        return 1
    else:
        return n * factorial(n - 1) # llamada recursiva

numero = int(input("Ingresa un numero para hayar el factorial: "))
print(factorial(numero))

# Ejercicio extra 2

def Fibonacci(n, x, a):
    y = a
    if n == 2:  # caso base
        return y
    elif n == 1:
        return 0
    else:
        z = x + y
        x = y
        y = z
        fi = Fibonacci(n - 1, x, y) # llamada recursiva
        return fi

posicion = int(input("Ingresa una posicion para la secuencia de fibonacci: "))
print(Fibonacci(posicion, 0, 1))
