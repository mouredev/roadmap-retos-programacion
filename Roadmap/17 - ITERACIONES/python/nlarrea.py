"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

# OPTION 1

print("\nOPTION 1: for loop")

for num in range(1, 11):
    print(num)


# OPTION 2

print("\nOPTION 2: while loop")

num = 1
while num <= 10:
    print(num)
    num += 1


# OPTION 3

print("\nOPTION 3: recursive function call")


def counter(start: int, stop: int) -> int:
    """Prints the numbers in the given range.

    Parameters:
    - `start`: The number where the counter starts to count (included).
    - `stop`: The number where the count stops (included).
    """

    print(start)

    if start >= stop:
        return stop

    counter(start + 1, stop)


counter(1, 10)
