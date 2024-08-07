#02 FUNCIONES Y ALCANCE
"""EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
    """
#Functions
def simple_function():
    print("funcion simple")
simple_function()

def return_function():
    return "funcion con retorno"
print(return_function())

def multiple_return_function():
    return "funcion", "multiple","retorno"
print(multiple_return_function())

def one_parameter_function(parameter):
    print(f"funciones con un solo {parameter}")
one_parameter_function("parametro")


def multiple_paramater_function(parameter_one="1", parameter_two= "2", *another_parameters):
    print(f"parameter one: {parameter_one} || parameter two:{parameter_two}")
    for parameter in another_parameters:
        print(parameter)
multiple_paramater_function()
multiple_paramater_function(parameter_two="two",parameter_one="one")
multiple_paramater_function("hola", "mundo", "hecho", "en", "python")

def multiple_named_parameters(**parameters):
    for index, parameter in parameters.items():
        print(f"index: {index}, value: {parameter}")

multiple_named_parameters(
    one= "hola", 
    two= "mundo",
    three= "python")

#Function in functions
def extern_function(param_1,param_2, param_3):
    
    def intern_function(_param_2, _param_3):
        return _param_2+ _param_3

    return lambda param_4, param_5:param_4+param_5+intern_function(param_2,param_3)+param_1

print(extern_function(1,2,3)(4,5)) #15

#Built in Functions
print(len("hola mundo")) # Character count
print(type("String"))
print(9.9)
print(10)
print(bin(111111))
print(int("45"))

#Local and Global Variables
variable = "Global"
def printable(variable):
    print(variable)

print(variable)
printable("Local")
print(variable)

"""DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda."""

def two_strings(_string_one, _string_two):
    count = 0
    for index in range(1, 101):
        text = ""
        if index%3 == 0:
            text+=_string_one
        if index%5 == 0:
            text+=_string_two
        if text == "":
            print(index)
            count+=1
        else:
            print(text)
    return count

print(two_strings("one","two"))