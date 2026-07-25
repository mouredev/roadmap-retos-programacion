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

# 1) Funciones básicas

# Sin parámetros ni retorno
def function1():
    print("Hola mundo")

function1()

# Con retorno
def function2():
    return "Hola mundo"

print(function2())

# Con uno o varios parámetros
def function3(name, surname):
    print(f'Hola, {name} {surname}')

function3('Daniel', 'Quiros')

# Con retorno y uno o varios parámetros
def function4(num1 = 3, num2 = 5):
    return num1 + num2

print(function4(1, 2))
print(function4())

# Con argumentos por defecto
def function5(*names): # El asterisco indica que se espera un número variable de argumentos
    for name in names: 
        print(f'Hola {name}')

function5('Dani', 'Africa', 'Paco', 'Jhon')

# Con un número variable de argumentos y palabras clave
def function6(**names):
    for key, name in names.items():
        print(f'Hola {name} ({key})')

function6(
    name='Dani', 
    surname='Quiros', 
    alias='DaniQB99',
    age=25
)

# 2) Funciones dentro de funciones

def outer_function():   
    def inner_function():
        print('Funciones internas: Hola, mundo')
    
    inner_function()

outer_function()


# Funciones propias del lenguaje (built-in)

print(len('Hola mundo')) # len() devuelve la longitud de una cadena
print(sum([1, 2, 3, 4, 5])) # sum() devuelve la suma de un vector
print(max([1, 2, 3, 4, 5])) # max() devuelve el mayor valor de un vector
print(min([1, 2, 3, 4, 5])) # min() devuelve el menor valor de un vector    
print(type('Hola mundo')) # type() devuelve el tipo de un objeto
print('Hola mundo'.lower()) # lower() devuelve una cadena en minúsculas
print('Hola mundo'.upper()) # upper() devuelve una cadena en mayúsculas

# Variables locales y globales

global_var = 'Python'

def hello_python():
    local_var = 'Hola'
    print(f'{local_var}, {global_var}')

print(global_var)
# print(local_var) # Error: local_var no esta definida fuera de la funcion
hello_python()

# 3) Función que reciba dos parámetros de tipo cadena de texto y retorne un número.
print('\n--- EJERCICIO EXTRA ---')

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers('Fizz', 'Buzz'))