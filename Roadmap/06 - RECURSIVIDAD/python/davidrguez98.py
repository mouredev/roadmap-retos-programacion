""" # #06 RECURSIVIDAD
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
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**. """

# EJERCICIO

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)

# DIFICULTAD EXTRA

def factorial(numero: int) -> int:
    if numero < 0:
        print("Los números negativos no son válidos")
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
print(factorial(10))



def fibonacci(num: int) -> int:
    if num <= 0:
        print("Los números negativos no son válidos")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
print(fibonacci(3))
