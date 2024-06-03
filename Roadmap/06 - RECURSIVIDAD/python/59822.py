'''  * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 * 
'''
def countdown(number : int):
    while number > 0:
        print(number, end=" ") 
        number-= 1
    print(f"\nEl número final es {number}")
    
countdown(52)

'''  * EXTRA:
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
'''
def factorial(numero : int):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero -1)
    #retorna la funcion hasta que llegue a 0

print(factorial(3))

## Fibonacci es la suma de los dos anteriores

def fibonacci(number : int):
    if  number <= 0:
        return "No se puede un negativo o cero"
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1)+fibonacci(number - 2)
    # retorna la funcion hasta que llegue a 0
    
print(fibonacci(3565))