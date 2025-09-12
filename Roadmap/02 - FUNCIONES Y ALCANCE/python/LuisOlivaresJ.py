"""
* - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
""" 

def my_dummy_func():
    """Una función sin parámetros ni retorno."""
    pass

my_dummy_func()  # A call to the function.

def saludar(name: str):
    """Una función con un parámetro."""
    print(f"Hola {name}.")

saludar("Luis")

def suma(x: int, y: int) -> int:
    """Una función con dos parámetros y un retorno."""
    z = x + y
    return z

print(suma(1,3))  # prints 4

# - Comprueba si puedes crear funciones dentro de funciones.

def line_eq(x):
    def mult(x, m):
        return m*x
    return mult(x, 2) + 1

print(line_eq(2))

#- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

print(sum([1,2,3]))

#Argument tuple packing
"""When a parameter name in Python function definition is preceded by an asterisk (*), 
it indicates argument tuple packing. Any corresponding arguments in the function call 
are packed into a tuple that the function can refer by the given parameter name.
"""

def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)
print("\n###########\nArgument tuple packing:\n")
f(1, 2, 3)

#- Pon a prueba el concepto de variable LOCAL y GLOBAL.

def main_function():
    local_variable = 5
    print("Inside main function")
    print(f"{local_variable=}")

my_global_variable = 10
main_function()
print("Outside the function")
print(f"{my_global_variable=}")

"""
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 """

def str_to_num(arg1: str, arg2: str):

    counter_substitution = 0

    for i in range(1, 16):

        if not(i%3):
            if not(i%5):
                print(arg1+arg2)
                counter_substitution += 1
            else:
                print(arg1)
                counter_substitution += 1

        elif not(i%5):
            print(arg2)
            counter_substitution += 1
        
        else:
            print(i)
    return counter_substitution

counter = str_to_num("Tres", "Cinco")
print(f"{counter=}")