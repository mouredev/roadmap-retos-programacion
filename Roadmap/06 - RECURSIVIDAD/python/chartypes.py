'''
# #06 RECURSIVIDAD
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

'''


def counting_down_to_zero(initial_number:int)->None:
    print(initial_number)
    if initial_number==0:
        return 0
    return counting_down_to_zero(initial_number-1)


def factorial(number:int) -> int:
    if number <= 1:
        return number
    return number * factorial( number-1 )    

def get_fibonacci_number_by_position(position:int)->int:
    number:int = 0
    if position == 1:
        return 1
    if position == 0:
        return 0
    number = get_fibonacci_number_by_position(position-1) + get_fibonacci_number_by_position(position-2)
    return number
   




# counting_down_to_zero(100)
# print(factorial(5))
# print(factorial(0))
# print(factorial(24))
# print(get_fibonacci_number_by_position(0))
# print(get_fibonacci_number_by_position(1))
# print(get_fibonacci_number_by_position(2))
# print(get_fibonacci_number_by_position(20) )
