# #02 Funciones y alcance

#simple
def greet ():
    print("¡Hola buenas!")
greet ()

# con retorno
def return_greet ():
    return "¡Hola buenas!"
print(return_greet ())

# con un argumento
def arg_greet(name):
    print(f"¡Hola, {name}!")
arg_greet ("Antonio")

# con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}!")
args_greet ("¡Hola", "Antonio")

# con argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"¡Hola, {name}!")
default_arg_greet("Antonio")
default_arg_greet()

# con argumento y return
def return_args_greet(greet, name):
    return f"{greet}, {name}!"
print(return_args_greet("Hola", "Antonio"))

# con retorno de varios valores
def multiple_return_greet():
    return "hola", "Python"
greet, name = multiple_return_greet()
print (greet)
print (name)

# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print (f"Hola, {name}!")
variable_arg_greet ("Python", "Antonio", "Devs", "Todos")

# Con número variable de argumento con palabra clave
def variable_key_arg_greet (**names):
    for key, value in names.items():
        print (f"{value} ({key})")
variable_key_arg_greet(Lenguaje="Python", nombre="Antonio", alias="Antoniomendozad", edad="29")

# Funciones dentro de funciones
def outer_function():
    def inner_function():
        print("Función interna: ¡Hola Python!")
    inner_function()
outer_function()

#funciones del lenguaje (built-in)
print(len("Antonio")) #7 letras len me da la cantidad de letras
print (type("Python"))
print (type("23"))
print (type(23)) #type dice el tipo 
print ("Antonio".upper()) #upper toma en este caso el texto a imprimir y lo coloca en mayúscula cerrada

# Variables locales y globales
global_var = "Python"

def hello_python():
    local_var = "hola"
    print (f"{local_var}, {global_var}!")
print(global_var)
#print (local_var) no se puede acceder desde fuera de la función
hello_python()

#extra

"""
def print_numbers(text_1, text_2) -> int:
    for number in range (1, 101):
        if number %3 == 0 and number % 5 == 0:
            print (text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
        

    print_numbers("Texto 1", "Texto 2")
"""