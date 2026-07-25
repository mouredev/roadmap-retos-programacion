# Función recursiva
def cuenta_atras(numero):
    if numero >= 0:
        print(numero)
        cuenta_atras(numero - 1)

cuenta_atras(100)

'''
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
'''
print("\nEjercicio de dificultad extra\n")

def factorial(num):
    result = 1
    i = 0

    def calculo(n):
        nonlocal result, i
        if n < 0:
            print("Los números negativos no son válidos.\n")
        elif n == 0:
            print(f"El factorial de 0 es 1\n")
        elif n > 0:
            i += 1
            result *= n
            calculo(n - 1)
        else:
            print(f"El factorial de {i} es {result}\n")

    calculo(num)

numero = int(input("Escribe el valor del factorial que quieras calcular: "))
factorial(numero)

def num_fibonacci(posicion):
    num1 = 0
    num2 = 1
    i = 2

    def suc_fibonnaci():
        nonlocal num1, num2, posicion, i
        if posicion < 0:
            print(f"Las posiciones negativas no son válidas.\n")
        elif posicion == 0:
            print(f"La posición 0 corresponde al número 0 de la sucesión de Fibonacci.\n")
        elif posicion == 1:
            print(f"La posición 1 corresponde al número 1 de la sucesión de Fibonacci.\n")
        elif posicion > i:
            copia = num2
            num2 += num1
            num1 = copia
            i += 1
            suc_fibonnaci()
        else:
            print(f"La posición {i} corresponde al número {num2} de la sucesión de Fibonacci.\n")
    
    suc_fibonnaci()
    
posicion = int(input("Escribe la posición del número de la sucesión de Fibonacci que desees: "))
num_fibonacci(posicion)