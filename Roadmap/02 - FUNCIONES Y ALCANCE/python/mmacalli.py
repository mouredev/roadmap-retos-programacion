"""
funciones definidas por el usuario
"""
#simple

def greet():
    print("hola, Python!")
    
greet()

#con retorno

def return_greet():
    return "Hola, Python"
print(return_greet())

#con argumento

def arg_greet(name):
    print(f"Hola, {name}!")
    
arg_greet("maca")

#con argumento predeterminado

def default_arg_greet(name="rucucu"):
    print(f"Hola, {name}!")
    
default_arg_greet("love")
default_arg_greet()

#con argumento y retorno

def return_arg_greet(greet, name):
    return f"{greet}, {name}!"
    
print(return_arg_greet("bonacera","pitufo"))
    
# con retorno de varios valores

def multiple_return_greet():
    return "hola", "Python"
greet, name = multiple_return_greet()
print(greet)
print(name)

def variable_arg_greet (*names):
    for name in names:
        print(f"Hola,{name}:")
variable_arg_greet("python","maca","loquito","barrio")

#con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")
        
variable_key_arg_greet (
    lenguaje ="python",
    name="maca",
    alias ="loquito",
    de_donde ="barrio",
    age= 49 
)
"""
funciones dentro de Funciones
"""
def outer_funcion():
    def inner_funcion():
        print("funcion interna: Hola, Python !")
    inner_funcion()

outer_funcion()
""" 
funciones del lenguaje (built-in)
"""

print (len("martincho"))
print(type("hola"))
print ("martincho".upper())

"""
Variables locales y globales
"""
global_var = "Python"
print(global_var)

def hello_python():
    local_var = "hola"
    print(f"{local_var}, {global_var}!")

print(global_var)

hello_python()


"""
extra
"""
def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range (1, 101):
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

print(print_numbers("Texto 1 ", "Texto 2"))
        






