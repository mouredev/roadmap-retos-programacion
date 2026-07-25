


#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).
#  */


     #recursividad , apliacion 
def factorial(n):
    if n == 1:
        return 1   #cuando 7*6*5*4*3*2 (llega a 1) se detiene y retorna el resultado
    else:
        return n * factorial(n - 1)
print(factorial(7))  # = 5040


def secuencia(n):
    if n == 5:
        return 5 # #cuando 7*6*5 (llega a 5) se detiene y retorna el resultado
    else:
        return n * secuencia(n - 1)
print(secuencia(7))     # = 210


def continu(n):
    if n == 20:
        return 20 # #cuando 7*6*5 (llega a 5) se detiene y retorna el resultado
    else:
        return n + continu(n - 1)
print(continu(50))  # 50+49+48+47.......+20 =1085


   #aplicando loops while:
x= 1
while x <= 100:
    print(x)  # imprime del 1 al 100
    x += 1  # Incrementamos la variable en 1 hasta ==100
   # print(x)  ## ojo, desde aqui del 2 al 101

  ##Imprime de 100 hasta 0
x = 100
while x >= 0:
    print(x)
    x -= 1 ## imprime del 100 al 0

   
   ####combinación de funcion con bucle while::###

def imprimir_numeros():
    x = 100
    while x >= 0:
        print(x)
        x -= 1
# Llamamos a la función
imprimir_numeros() #imprime de 100 hasta 0


# aplicando para valores de fibonacci

def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia
print(fibonacci(10))     # Generar los primeros 10 números de la secuencia de Fibonacci
