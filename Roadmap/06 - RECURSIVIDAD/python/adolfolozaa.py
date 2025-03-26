'''
RECURSIVIDAD: Funcion que se llama a ella misma

EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
 '''
def coutdown(number):
    if number >= 0:
        print(number)
        coutdown(number - 1)
        

coutdown(100)

'''

 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 '''

# Factorial
def factorial(numero: int)->int:
    if numero < 0:
        print(' los numeros negativos no son validos')
        return 0
    elif numero == 0:
        return 1
    else:
        return numero *factorial(numero -1)
    
numero = 15
print('--------------------')
print(f'El factorial de {numero} es {factorial(numero)}')



#Fibonacci
def fibona(numero: int) -> int: 
    if numero <= 0:
        print(' debe ser un numero mayor a cero')
        return 0
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibona(numero - 1) + fibona(numero - 2)

print('--------------------')
print('Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición)')
posicion = input('Ingrese la posicion deseada?  ')
print(fibona(int(posicion)))
             