
'''
EJERCICIO:
  Entiende el concepto de recursividad creando una función recursiva que imprima
  números del 100 al 0.
'''

# FUNCIONES RECURSIVAS
num:int = 100

def func_recursiva(n: int) -> None:
    if n >= 0:
        print(n)
        func_recursiva(n-1)


func_recursiva(num)


'''
DIFICULTAD EXTRA (opcional):
   Utiliza el concepto de recursividad para:
   - Calcular el factorial de un número concreto (la función recibe ese número).
   - Calcular el valor de un elemento concreto (según su posición) en la 
     sucesión de Fibonacci (la función recibe la posición).
'''

print('\n--- EJERCICIO EXTRA ---\n')

# FACTORIAL
def factorial(n: int) -> int:
    if n < 0:
        print('El numero debe ser positivo')
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print('Factorial de 5: ' + str(factorial(5)))
print('Factorial de 0: ' + str(factorial(0)))
print('Factorial de 24: ' + str(factorial(24)))

# FIBONACCI SIMPLE
def fibonacci_simple(n: int) -> int:
    if n < 0:
        print('El numero debe ser positivo')
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_simple(n - 1) + fibonacci_simple(n - 2) # Devuelve el resultado de la suma de los dos anteriores
    
print('\nEJEMPLO DE FIBONACCI SIMPLE\n')
print('Fibonacci de 5: ' + str(fibonacci_simple(5)))
print('Fibonacci de 0: ' + str(fibonacci_simple(0)))
print('Fibonacci de 24: ' + str(fibonacci_simple(24)))

# FIBONACCI COMPLEJO    
def fibonacci_complejo(n: int) -> list[int]:
    if n < 0:
        print('El numero debe ser posit ivo')
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibo = [0, 1]
        for i in range(2, n):
            fibo.append(fibo[i - 1] + fibo[i - 2]) 
        return fibo # Devuelve la lista de los resultados hasta la posicion n de la serie
    
print('\nEJEMPLO DE FIBONACCI COMPLEJO\n')
print('Fibonacci de 5: ' + str(fibonacci_complejo(5)))
print('Fibonacci de 0: ' + str(fibonacci_complejo(0)))
print('Fibonacci de 24: ' + str(fibonacci_complejo(24))) 