"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""


def measure_time(function):
    def wrapper(*args, **kwargs):
        """Función de lógica del decorador."""

        import time

        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Required time: {round(end - start, 4)} seconds")

        return result

    # Las variables del decorador se colocarían aquí
    # ...

    return wrapper


""" Cada decorador funciona como una instancia diferente para cada función
decorada, por eso podemos crear "variables" dentro del decorador.
Cada vez que se llame a la misma función, la variable no se resetea. """


@measure_time
def sum_two_values(num_one: int, num_two: int):
    import time

    time.sleep(3)

    return num_one + num_two


print(sum_two_values(10, 5))
""" prints:
Required time: 3.0013 seconds
15
"""


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""

counter = 0


def count_calls(function):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        function(*args, **kwargs)
        print(
            f"Calls number for function '{function.__name__}': {wrapper.counter}"
        )

        return function

    # Variable del decorador -> se ejecuta 1 vez por función decorada
    wrapper.counter = 0

    return wrapper


@count_calls
def print_message(message: str = "Hello there!"):
    print(message)


@count_calls
def another_function():
    pass


print_message()
print_message()
another_function()
print_message()
another_function()
