"""# #06 RECURSIVIDAD
> #### Dificultad: Difícil | Publicación: 05/02/24 | Corrección: 12/02/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
 """

def cuentaregresiva(numero:int):
    if numero >= 0:
        print(numero)
        cuentaregresiva(numero-1)

cuentaregresiva(100)

def factorial (numero:int):
    if numero<0:
        print ("no se puede hacer el factorial de un numero negativo")
        return 0
    elif numero ==  0:
        return 1
    
    return numero * factorial(numero-1)
      

print(factorial(6))

def fibonacci (numero:int)-> int:
    if numero < 0:
        print ("no puede ser menor que cero")
        return 0
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
         return fibonacci(numero-1) + fibonacci (numero-2)

print(fibonacci(10))