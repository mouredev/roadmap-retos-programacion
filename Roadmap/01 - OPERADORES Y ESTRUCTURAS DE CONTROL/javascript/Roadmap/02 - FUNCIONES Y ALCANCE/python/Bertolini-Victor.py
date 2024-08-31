"""  
/*
    EJERCICIO:
        1) Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
            Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
        2) Comprueba si puedes crear funciones dentro de funciones.
            Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
            Pon a prueba el concepto de variable LOCAL y GLOBAL.
            Debes hacer print por consola del resultado de todos los ejemplos.
            (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

    DIFICULTAD EXTRA (opcional):
        3) Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
            - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
            - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
            - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

    Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
    Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/
"""

# 1) 
    # 1. Función simple: Función sin parámetros ni retorno. / Simple Function: Without parameters and return.

def hello_world():
    print("Hello World!")

hello_world()

    # 2. Función con retorno: Función sin parámetros pero con retorno. / Function with return: Function without parameters but with return.
def hello_world_with_return():
    return ("Hello World!")

print(hello_world_with_return())

    # 3. Función con un argumento: Función con un parámetro pero sin retorno. / Function with parameters: Function with parameters but without return.
def hello_world_with_param(name):
    print("Hello, " + name + "!")

hello_world_with_param("Victor")

    # 4. Función con argumentos: Función con múltiples parámetros pero sin retorno.
def hello_world_with_params(name, surname):
    print("Hello, " + name + " " + surname + "!")

hello_world_with_params("Victor", "Bertolini")

    # 5. Función con un argumento predeterminado: Función con un parámetro con valor predeterminado.
    # Function with a assigned parameter: Function with a parameter with a default value.
def hello_world_with_param_predefined(name = "Victor", surname = "Bertolini"):
    print("Hello, " + name + " " + surname + "!")

hello_world_with_param_predefined()

    # 6. Función con argumentos y retorno: Función con uno o más parámetros y con retorno.
    # Function with parameter and return: Function with both parameter and return.
def hello_world_with_both(name):
    return("Hello, " + name + " ")

print(hello_world_with_both("Victor"))

    # 7. Función con retorno de varios valores: Función que devuelve múltiples valores.
def ret_many_values():
    return 1, 2, 3, 4

print(ret_many_values())

    # 8. Función con un número variable de argumentos: Función que puede tomar un número variable de argumentos.
    # Fuction with a variable number of arguments: Function that could take a variable number of arguments.
def many_variables(*languages):
    for language in languages:
        print(f"Hello, , {language}!")

many_variables("Pythom", "Java", "Ruby", "PHP", "JavaScript", "C#")

    # 9. Función con un número variable de argumentos con palabra clave: Función que puede tomar un número variable de argumentos de palabras clave.
    # Function with a variable number of keyword arguments: Function that can take a variable number of keyword arguments.
def many_variables_with_keywords(**pokemons):
    for key, value in pokemons.items():
        print(f"{value} is the {key}!")


many_variables_with_keywords(
    name ="Pikachu",
    type ="Electric",
    trainer ="Ash",
    level = 100
)

# 2) 
    # Fucntiones anidadas / Nested functions.
        # Si es posible crear funciones dentro de otras.
        # Yes, It's possible to create functions inside other functions.
def outside_func():
    def inside_func():
        print("I'm an inside function.")
    inside_func()

outside_func()

    # Funciones del lenguaje / In-Build functions.
""" 
    Existen muchas funciones por defecto de Python, aca se mostraran algunas no mas. 
    Para mas informacion: https://docs.python.org/es/3.9/library/functions.html#len
    --------------------------------------------------------------------------------
    There are many different in-build functions in Python, here only a few will be used.
    For more information: https://docs.python.org/es/3.9/library/functions.html#len
"""

print(len("Hello, world!")) #It should print the number 13 / Deberia imprimir el numero 13.
print(str(10 + 15)) #It should print the number 25 / Deberia imprimir el numero 25.

numeros = [1, 2, 3, 4, 5] # Sumar los elementos de una lista / Sum the elements of a list.
suma = sum(numeros)
print(suma)  # Imprime: 15 / Print: 15.

numeros = [1, 2, 3, 4, 5] # Sumar los elementos de una lista con un valor inicial. Sum the elements in the list with a beginning value.
suma = sum(numeros, 30)
print(suma)  # Imprime: 45 / Print: 45.


    # Variables globales y locales. / Local and global variables.
""" 
    Las variables globales son las que se crean simplemente al crear una fuera de cualquier tipo de 
    estructura de control o similar del lenguage, y se pueden acceder desde cualquier parte del codigo. 
    Mientras que las locales son las que se crean cuando usas variables dentro de funcion, o similar, 
    pero que no se pueden "ver" desde otra parte del codigo que no sea dentro de donde fue declara.
    ---------------------------------------------------------------------------------------------------
    The global variables are the ones that are used when you simply declare a variable in any part of the
    code that is not a function or a structure of contron of Python, and they can be used from any part of
    the code. Meanwhile, local variables are the ones that are declare inside of functions, and similar, 
    and can be used only inside the function from which they were declared.
"""

this_is_a_global_variable = 14

def func():
    this_is_a_local_variable = True
    if (this_is_a_local_variable):
        print(this_is_a_global_variable)

func()

# 3) EXTRA
""" 
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
        - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
        - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
        - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
def print_numbers(string1, string2) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0:
            print(string1)
        elif i % 5 == 0:
            print(string2)
        elif i % 5 == 0 and i % 3 == 0:
            print(string1 + " " + string2)
        else:
            print(i)
            count += 1
    return count

print("")
print("")
print("")

numeros_impresos = print_numbers("Fizz", "Buzz")
print("Se imprimieron", numeros_impresos, "numeros.")