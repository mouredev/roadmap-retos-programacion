#EJERCICIO:
#- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
#"Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#Comprueba si puedes crear funciones dentro de funciones.
#Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#Pon a prueba el concepto de variable LOCAL y GLOBAL.
#Debes hacer print por consola del resultado de todos los ejemplos.
#(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

#DIFICULTAD EXTRA (opcional):
#Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#"Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#La función retorna el número de veces que se ha impreso el número en lugar de los textos.

# Funcion Simple
def greet():
    print("Hola")

greet()
greet()

# Funcion con retorno

def return_greet():
    return "Hola, Py"

print(return_greet())

#Funcion con un argumento

def arg_greet(name):
    print(f"hola, {name}")

arg_greet("Elder")

#Funcion con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}")

args_greet("Hi", "Elder")

#Funcion con un argumento predeterminado

def default_arg_greet(name="Nombre Predet"):
    print(f"hola, {name}")

default_arg_greet("Elder")
default_arg_greet()

# Funcion con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Py"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Funcion con numero variable de argumentos o parametros

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Python", "Elder", "Comunidad")

# Funcion con numero variable de argumentos con palabra clave

def variable_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {value}({key})")

variable_arg_greet(Lenguaje="Python", name="Elder", alias="Comunidad", age=36)

# Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("Funcion interna")
    inner_function()
    
outer_function()

# Funciones del lenguaje (Built-in)

print(len("Elder"))
print(type("Elder"))
print("Elder".upper())

# Variables locales y globales (Ambitos - scope)

global_var = "Python"
print(global_var)

def hello_python():
    local_var = "Hello"
    print(f"{local_var}, {global_var}")

hello_python()

# Dificultad_extra

def print_numbers(par1,par2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(par1 + par2)
        elif number % 3 == 0:
            print(par1)
        elif number % 5 == 0:
            print(par2)
        else:
            print(number)
            count ++ 1
    return count

print(print_numbers("Fizz","Buzz"))