# @author: Mhayhem

# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

def withoiut_params():
    print("Esta función no tiene parámetros ni retorno.")

def whith_one_param(param):
    print(f"Esta es una función con {param}.")

def whith_two_params(param1, param2):
    print(f"Esta función tiene {param2} {param1}.")

def with_return(param):
    return f"Esta función tiene {param}."
"""
usando como parametro *args y **kwargs podremor flexibilizar el numwero de parámetros
que recibe nuestra función"""

def with_multiple_params_without_name(*args): # nos permite pasarle a la funcion un numero de parámetros sin nombre, *args es una tupla
    print(f"Esta funcion puede recibir {len(args)} argumrntos posicionales.")
    print(f"Los parámetros son: {args}.")

def with_multiple_params_with_name(**kwargs): # también nos permite pasarle un número variable de parámetros pero en este caso con nombre, **kwargs es un diccionario
    print(f"Esta funcion puede recibir {len(kwargs)} argumentos con nombre.")
    print(f"Los parámetros son: {kwargs}.")

def with_multiple_returns():
    return "Este es el primer retorno.", "Y este es el segundo retorno."

# - Comprueba si puedes crear funciones dentro de funciones.

def function_inside_function():
    print("Esta función contiene otra dentro de su bloque de código.")
    
    def inner_function():
        print("Esta es la función que esta dentro de la función principal.")
    inner_function()
def function_with_lambda(param): # también puede contener una función lambda
    func_lambda = lambda param: param ** 2
    return f"Función lambda que eleva al cuadrado un número: {func_lambda(param)}"

# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

# de hecho ya hemos usado una función propia de python como es print() pero pondre otro ejemplo
python_func = f"Imprimimos el mayor número de una lista usando la funcion propia de python 'max': {max([10,20,30,40])}."

# - Pon a prueba el concepto de variable LOCAL y GLOBAL.

global_var = "Esta es una variable global"
def local_and_global_var():
    local_var = "Esta es una variable local"
    print(f"Variable local: {local_var} solo es accesible dentor de la función.")
    print(f"Variable global: {global_var} es accesible desde cualquier parte del código.")


# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
withoiut_params()
whith_one_param("un parámetro")
whith_two_params("parámetros", 2)
print(with_return("Un retorno"))
with_multiple_params_without_name("coche", "avión", "barco")
with_multiple_params_with_name(name="Dany", age=42, city="Valladolid")
print(with_multiple_returns())
function_inside_function()
print(function_with_lambda(9))
print(python_func)
local_and_global_var()
#
# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def fizzbuzz(text_1, text_2):
    count = 0
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(f"{text_1}{text_2}")
        elif n % 3 == 0:
            print(text_1)            
        elif n % 5 == 0:
            print(text_2)
        else:
            print(n)
    return count

print(fizzbuzz("Fizz", "Buzz"))
