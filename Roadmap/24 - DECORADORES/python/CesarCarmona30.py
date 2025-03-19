'''
  EJERCICIO
'''

"""
Ejercicio
"""


def print_call(function):
    def print_function():
        print(f"La función '{function.__name__}' ha sido llamada.")
        return function
    return print_function


@print_call
def example_function():
    pass


@print_call
def example_function_2():
    pass


@print_call
def example_function_3():
    pass

example_function()
example_function_2()
example_function_3()


'''
  EXTRA
'''

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función '{function.__name__} se ha llamado {counter_function.call_count}' veces.")
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
example_function_4()
example_function_5()
example_function_4()
example_function_5()
