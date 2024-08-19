## Funciones definidas

# Funciones simples - Bloque de código que ejecuta ciertas utilidades.
def greet():
    print("Hola, Python!")
greet()

# Funciones con retorno - Bloque de código que retorna un valor determinado.
def greet_return():
    return print("Hola, Python")
greet_return()

# Funciones con argumentos - Bloque de código que puede recibir un argumento en específico y basar la función basado en ese valor. Le pasamos 'name' a 'greet_arg' y cuando llamemos la función, podemos especificar el valor de name.
def greet_arg(name):
    print(f"Hola, {name}")
name = 'Python!'
greet_arg(name)

# Funciones con argumentos predeterminados - Igual que el anterior, pero esta vez podemos asignar un valor predeterminado que será utilizado si no hay otro valor asignado. 
def def_greet_arg(name='Python!'):
    print(f"Hola, {name}")

def_greet_arg('Bris') # Devuelve 'Bris' porque es el valor que le asignamos.
def_greet_arg() # Devuelve Python ya que es el valor predeterminado.

# Funciones con retorno de varios argumentos
def multiple_return_greet(): # Función que a pesar de que no recibe ningún argumento, puede retornar varios.
    return 'Python', 'Hola', 32 # Almacenamos tres valores diferentes separados por comas. 

name, greet, age = multiple_return_greet() # Destructuramos los valores en orden posicional.
print(name)
print(greet)
print(age)

# Funciones con un número variable de argumentos

def mult_arg_greet(*names): # Podemos decirle que aparte del name, puede recibir mas argumentos.
    for name in names:
        print(f"Hola {name}") # Iterare sobre cada name dentro de los names que reciba.

mult_arg_greet('Little', 'Mabbit', 'Hi')

## Función dentro de una función

def outer_function(): # Creamos la función externa
    def inner_function(): # Creamos la función interna
        name = 'English'
        print(f'Hi {name}! Printing inner function')
    inner_function() # Llamamos la función interna al final de la función externa para que se ejecute lo que está dentro.
    print(f'Y luego, esta es la función externa')

outer_function()

## Funciones dentro del lenguaje. - Funciones que ya están construidas dentro del lenguaje.

print(len('LittleMabbit')) # Cuenta los elementos del string.
print(type('LittleRat')) # Muestra el tipo de dato.
print(sorted('bcdsaw')) # Ordena en orden alfabético
print('littlemabbit'.upper())
print('LITTLEMABIT'.lower())
print('LEARNINGPYTHON'.isupper())

## Variables locales y variables

global_var = 'Python' # Variable que puede ser asignada a todo código debajo de él

def global_var_function():
    local_var = 'Hola' # Variable que solo tiene como scope el bloque en el que está.
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) # Esta no la encuentra porque solamente fue declarada dentro del bloque de código de la función.
global_var_function()

'''
EXTRA: 
 * - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''
def ejercicio(t1, t2):
    # Inicializamos la variable del conteo fuera del bucle.
    c = 0
    # Imprime numeros del 1 al 100.
    for i in range(0, 101):
        # Si el numero es multiplo de 3 y de 5, concatena la cadena de texto.
        if i % 3 == 0 and i % 5 == 0:
            print(f'{t1}{t2}')
        # Si el numero es multiplo de 3, muestra t1
        elif  i % 3 == 0:
            print(t1)
        # Si el numero es multiplo de 5, muestra t2
        elif i % 5 == 0:
            print(t2)
        # Numero de veces que se imprime un número en vez de texto.
        else:
            print(i)
            c += 1
    # Función retorna el conteo de veces que se devolvió un numero en vez de texto.
    return c

print(ejercicio('Fizz', 'Buzz'))