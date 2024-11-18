
# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *



#1. Funcion sin parámetros y sin retorno

def hello():
    print("Hello")

hello()

#2. Funcion con un parámetro

def date_person(name):
    print(f"Hello, {name}")

date_person("bryan")

#3. Funcion con multiples parametros y sin retorno

def dates_person(name, edad):
    print(f" my name is {name}, y mi edad es {edad}")

dates_person("bryan", 27)


#4. Funcion con retorno

def multiply_number(a,b):
    return a * b
producto = multiply_number(4,6)
print(f"The product of 4 an 6 is {producto}")


#5. Funcion dentro de otra funcion

def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 3

result =outer_function(5)
print(f"Result of outer_function(5) is {result}")



#6. Uso de una funcion predefinida en python

def get_length_of_string(s):
    return len(s)

length = get_length_of_string("python")
print(f"the length of the string 'Python' is {length}")

#7. Variables gobales y locales

global_variable = 10

def local_vs_global():
    global global_variable
    local_variable = 5
    global_variable = 20  # Modifica la variable global
    print(f"Local variable is {local_variable}")
    print(f"Global variable inside function is {global_variable}")

local_vs_global()
print(f"Global variable outside function is {global_variable}")


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


def extra(text1, text2):
    array =[]
    for i in range(1,101):
        if i  % 3 == 0 & i % 5 == 0:
            array.append(text1 + text2)
        elif i % 3 == 0:
            array.append(text1)
        elif i % 5 == 0:
            array.append(text2)
        else:
            array.append(i)
    print(array)

extra("mult3", "mult5")

