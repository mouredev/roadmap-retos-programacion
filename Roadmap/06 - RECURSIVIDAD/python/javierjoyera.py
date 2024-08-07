##06 RECURSIVIDAD

#Funcion Recursiva que imprime del 100 al 0
def imprimir_recursivo(n): 
    if n >= 0:
        print(n)
        #Llamada recursiva en la cual le restamos 1 al valor de n
        imprimir_recursivo(n-1)
    else:
        return
    
#Llamada a la funcion
imprimir_recursivo(100)

#Factorial de un numero
'''
El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n.

n! = n * (n-1) * (n-2) * ... * 1

n! = n * (n-1)!

Ejemplo:
5! = 5 * 
4 * 3 * 2 * 1 = 120
'''
def function_factorial(n):
    if n == 0:
        return 1
    else:
        return n * function_factorial(n-1)
    
#ejemplo
my_number = 5
print("El factorial de %d es %d" % (my_number, function_factorial(my_number)))

#Calcular el valor de un elemento (según su posición) de la serie de Fibonacci
'''
La sucesión de Fibonacci es una sucesión infinita de números naturales que comienza con los números 0 y 1, y a partir de estos, 
cada término es la suma de los dos anteriores.
'''
def function_fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function_fibonaci(n-1) + function_fibonaci(n-2)
    
#Ejemplo
my_number = 7
print("El número de la serie de Fibonacci en la posición %d es %d" % (my_number, function_fibonaci(my_number)))

print("---------------------------------------------------")
    
#Ejemplo con entrada por terminal
print("Ingresa la posición del número de la serie de Fibonacci que deseas calcular")
my_number = int(input())
print("El número de la serie de Fibonacci en la posición %d es %d" % (my_number, function_fibonaci(my_number)))
