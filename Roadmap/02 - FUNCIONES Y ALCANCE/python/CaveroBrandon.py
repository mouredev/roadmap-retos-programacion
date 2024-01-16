import time

"""
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
"""


# **** Function without parameters or return ****
def small_triangle():
    global global_counter
    global_counter = global_counter - 1
    print('**** Function without parameters or return ****')
    print('  x  ')
    print(' xxx  ' + '\n')


# **** Function with one parameter no return ****
def draw_money(qty):
    global global_counter
    global_counter = global_counter - 1
    print('**** Function with one parameter no return ****')
    print('$' * qty + '\n')


# **** Function without parameter and with a return ****
def get_current_year() -> str:
    global global_counter
    global_counter = global_counter - 1
    print('**** Function without parameter and with a return ****')
    return time.asctime()[-4:]


# **** Function with one parameter and one return ****
def is_even(num) -> bool:
    global global_counter
    global_counter = global_counter - 1
    print('**** Function with one parameter and return ****')
    if num % 2 == 0:
        return True
    else:
        return False


# **** Function with multiple parameters, multiple returns and using functions within the function ****
def register_user(name='N/A', lastname='N/A', age=0) -> tuple:
    def is_older(age):
        if age >= 18:
            return True
        else:
            return False

    def get_id(name, lastname, age):
        result = name[0:3] + lastname[0:3] + str(age)
        return result

    global global_counter
    global_counter = global_counter - 1
    print('**** Function with multiple parameters, multiple returns and using functions within the function ****')
    if name != 'N/A':
        name = name.upper()
    if lastname != 'N/A':
        lastname = lastname.upper()
    full_name = name + ' ' + lastname

    return get_id(name, lastname, age), is_older(age), full_name


# **** Recursive function ****
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


"""
# DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""


def extra_difficulty(for_three='Tic', for_five='Toc') -> int:
    local_counter = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(for_three + for_five, end=',')
        elif i % 3 == 0:
            print(for_three, end=',')
        elif i % 5 == 0:
            print(for_five, end=',')
        else:
            print(i, end=',')
            local_counter = local_counter + 1
    return local_counter


global_counter = 10
print('The global counter started with a value of: ' + str(global_counter))

# **** Build in function ****
print('**** Build in function ****')
print("'print' is a build in function in Python" + '\n')

small_triangle()  # Function without parameters or return

draw_money(15)  # Function with one parameter no return

print(get_current_year() + '\n')  # Function without parameter and with a return

print(str(is_even(15)) + '\n')  # Function with one parameter and one return

(user_id, is_user_older, full_name) = register_user(name='Brandon', lastname='Cavero', age=15)  # Function with multiple parameters, multiple returns and using functions within the function
print('ID: ' + user_id)
print('Is member older: ' + str(is_user_older))
print('Full Name: ' + full_name + '\n')

print('**** Recursive function ****')
print('The result of the factorial of 5 is: ' + str(factorial(5)) + '\n')  # Recursive function

print('**** lambda function ****')
reduce_global = lambda x: global_counter - x  # lambda function
global_counter = reduce_global(1)

print('The global counter finishing with a value of: ' + str(global_counter) + '\n')  # Global variable test

print('****  Extra difficult ****')
extra = extra_difficulty(for_three='Zip', for_five='Zap')  # Extra difficult
print('\nThe number of times a number is printed instead of text: ' + str(extra))
