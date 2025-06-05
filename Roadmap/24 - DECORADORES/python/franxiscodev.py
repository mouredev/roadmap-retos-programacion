'''
Patrones de diseño
DECORADORES - decorator - wrapper
Extender la funcionalidad de una función sin modificar la original
'''


def print_call(function):
    def print_function():
        print(f"La función *{function.__name__}* ha sido llamada ")
        return function
    return print_function


@print_call
def example_function_1():
    # print("La función example_function ha sido llamada interna")
    pass


def example_function_2():
    # print("La función example_function_2 ha sido llamada")
    pass


def example_function_3():
    # print("La función example_function_3 ha sido llamada")
    pass


example_function_1()
example_function_2()
example_function_3()
'''
Extra
decorator crea una instancia única por eso al volver a llamarlo no se reinicia la variable
'''


def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función *{function.__name__}* se ha llamado {counter_function.call_count} veces ")
        return function

    counter_function.call_count = 0
    return counter_function


@call_counter
def example_function_4():
    pass


@call_counter
def example_function_5():
    pass


example_function_4()
example_function_4()
example_function_4()
example_function_5()
