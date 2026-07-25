"""
Funciones definidas por el usuario
"""

# Simple
def greet():
    print("Hola, Python!")
greet()


# Con retorno
def return_greet():
    return "Hola, Pyhton!"
greet = return_greet()
print(greet)


# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}!")
arg_greet("Hosi")


# Con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}!")
args_greet("Hola","Hosi")
args_greet(name="Hosi",greet="Hola") #si le digo qué es cada elemento, lo imprime en orden


# Con un argumento predeterminado
def default_arg_greet(name="Hosi"):
     print(f"Hola, {name}!")

default_arg_greet ("Hosi")
default_arg_greet () #como no le hemos introducido un parámetro, imprime el por defecto


# Con argumentos y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hola", "Hosi"))


# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)


# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Brais", "Comunidad") #puedo pasar la cantidad de argumentos que me de la gana

# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names): #cada argumento estará formado por una clave y un valor
    for key,name in names.items():
        print(f"{name}({key})!")

variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias= "Moueredev",
    edad=36
)


'''
Funciones dentro de funciones
'''

def outer_function():
    def inner_function():
        print("función interna: Hola, Python !")
    inner_function()
    
outer_function()


'''
Funciones del lenguaje (built-in)
'''

print(len("Mouredev")) #nos cuenta la cantidad de datos
print(type("Mouredev")) #nos dice el tipo de variable que es
print("Mouredev".upper()) #modifica el dato y lo escribe en mayúscula


'''
Variables locales y globales
'''

global_var="Python"

print(global_var)

def hello_python():
    local_var = "Hola" #esta variable, como es local, solo funciona dentro de la función
    print(f"{local_var}, {global_var}!")

# print(local_var) No se puede acceder desde fuera de la función

hello_python()


'''
Extra
'''
'''
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

def print_numbers(text_1,text_2)->int: #la función devolverá un número entero al final
    count = 0
    for num in range (1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(text_1 + text_2)        
        elif num % 3 == 0:
            print(text_1)  
        elif num % 5 == 0:
            print(text_2) 
        else:
            print(num)
            count += 1
    return (count)

print(print_numbers("Fizz","Buzz"))




