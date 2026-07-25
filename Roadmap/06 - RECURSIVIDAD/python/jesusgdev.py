'''
EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
   números del 100 al 0.
  
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
     sucesión de Fibonacci (la función recibe la posición).
'''


def countdown(num):
    print(num)

    if num == 0:
        return
    
    countdown(num - 1)

countdown(100)


'''
Extra
'''

# Factorial de un numero

print("")

def factorial(num):
    if num < 0:
        return print("Los numeros negativos no son validos")
    elif num == 0 or num == 1:
        result = 1
        print (result)
    elif num > 1:
        result = num * factorial(num - 1)
        print(result)
    return result

factorial(-1)

# Secuencia de fibonacci

print("")

def fibonacci(position):
    if position <= 0:
        return print("La posicion tiene que ser mayor que 0")
    
    def fibonacci_serie(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci_serie(n - 1) + fibonacci_serie(n - 2)
        
    for i in range(1, position + 1):
        print(fibonacci_serie(i))

fibonacci(5)