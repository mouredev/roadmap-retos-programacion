
#/*
# * EJERCICIO:
# * Entiende el concepto de recursividad creando una función recursiva que imprima
# * números del 100 al 0.

def cuenta_regresiva(numero: int):
    print(numero)
    numero -= 1
    if numero >= 0:
        cuenta_regresiva(numero)

cuenta_regresiva(100)

# *
# * DIFICULTAD EXTRA (opcional):
# * Utiliza el concepto de recursividad para:
# * - Calcular el factorial de un número concreto (la función recibe ese número).
# * - Calcular el valor de un elemento concreto (según su posición) en la 
# *   sucesión de Fibonacci (la función recibe la posición).
# */

def calcular_factorial(numero: int):
    if numero == 1:
        return numero
    else:
        return numero * calcular_factorial(numero - 1)

print(str(calcular_factorial(4)))

def calcular_posicion_en_secuencia_fibonacci(posicion: int):
    
    def generar_fibonacci(posicion_maxima: int, secuencia = [1,1]):
        if len(secuencia) == posicion_maxima:
            return secuencia
        else:
            secuencia.append(secuencia[-1] + secuencia[-2])
            return generar_fibonacci(posicion_maxima, secuencia)
    
    return generar_fibonacci(posicion)[posicion-1]

posicion = 10
print("En la secuencia de Fibonacci el número en la posición " + str(posicion) + " es: " + str(calcular_posicion_en_secuencia_fibonacci(posicion)))

