'''
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 '''

def imprimir_numeros(n):
    if n < 0:
        return
    else:
        print(n)
        imprimir_numeros(n - 1)

# Llamamos a la función con el valor inicial de 100
imprimir_numeros(100)
# Esto nos imprimirá de los numero de 100 a cero de manera descendiente. 

'''
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 '''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero_factorial = 5
resultado_factorial = factorial(numero_factorial)
print(f"El factorial de {numero_factorial} es {resultado_factorial}")

'''
* - Calcular el valor de un elemento concreto (según su posición) en la 
*   sucesión de Fibonacci (la función recibe la posición).
'''

# Tomando en cuenta la formula de la sucesión de Fibonacci:
#La fórmula matemática que describe la sucesión de Fibonacci es:

# F(n)=F(n−1)+F(n−2)

# Donde F(n) es el número en la posición y n de la secuencia de Fibonacci.
#Tenemos que sumar las posiciones acertada primero para poder calcular despues el valor de un elemento concreto.
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

posicion_fibonacci = 6
resultado_fibonacci = fibonacci(posicion_fibonacci)
print(f"El elemento en la posición {posicion_fibonacci} de la sucesión de Fibonacci es {resultado_fibonacci}")

