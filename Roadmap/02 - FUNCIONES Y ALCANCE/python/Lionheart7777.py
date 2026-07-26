""" Funciones dentro de Funciones
def f_principal(nombre):
    def f_interno ():
     print(f"hola {nombre}")

    f_interno()

f_principal("Ana") """
     


""""
num = 10 # variable global

def reinicio():
    global num
    num=20 # variable local

print(num) 
reinicio()
print(num) """
 
""""
valor = 10

def funcion():
    valor = 20
    print(valor)

funcion() # local
print(valor) # global    """ 

"""
FUNCIONES DEFINIDAS POR EL USUARIO """

# Simple
def greet():
    print("hola python")
greet() 

# Con Retorno
def return_greet():
    return "HOLA PYTHON"
greets = return_greet()
print(greets)

# Con un argumento

def arg_greet(name):
    print(f"Hola {name}")

arg_greet("Richard")


# Con varios Argumentos

def args_greet(greet,name):
    print(f"{greet}, {name} ")

args_greet("Hello", "Ricardo")    

# Con un argumento predeterminado

def default_arg_greet(name="Python"):
    print(f"Hola,{name}")

default_arg_greet("Richi")
default_arg_greet()


# Con argumentos y RETURN

def return_args_greet(greet, name):
    return f"{greet} {name}"

print(return_args_greet("Morning","Fiorella"))

# Con retorno de varios valores

def multiple_return_greet():
    return "hello", "Python"

saludo, name =multiple_return_greet()
print(saludo)
print(name)

# Con un numero variable de argumentos

def variable_args_greet(*names):
    for name in names:
        print(f"HELLO, {name}")

variable_args_greet("Fiorella","Alejandrina","Jerry","Tracy")  

# Con un numero variable de argumentos con PALABRA CLAVE

def variable_key_args_greet(**names):
    for key, value in names.items():
        print(f"HELLO, {value} ({key})")

variable_key_args_greet(
    mayor="Fiorella",
    Usa="Alejandrina",
    Tragon="Jerry",
    Pachi="Tracy",
    Edad= 67
    )

"""
Funciones dentro de Funciones
"""

def outer_function():
    def inner_function():
        print("Función Interna : HHolaa PPython")
    inner_function()
outer_function() 

"""
Funciones del Lenguaje (built-in)"""

print(len("JUlia"))
print(type(125))
print("Julia".upper())


"""
Variables globales y locales
"""

global_var = "pythoN"



def hello_python():
    local_var = "HI"
    print(f"{local_var}, {global_var}")
    print(local_var)

print(global_var)
# print(local_var)  NO SE PUEDE ACCEDER DESDE FUERA DE LA FUNCION
hello_python() 

# iterar sobre un número
for i in range(1,10):  # 0, 1, 2
    print(i)

# iterar sobre un diccionario

edades = {"ana": 10, "pedro":20}
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")

#iterar sobre una lista

frutas = ["manzana", "banana", "cereza"]
for frutitas in frutas:
    print(frutitas)

# obtener índice y valor usando enumerate
colores = ["rojo", "azul", "amarillo"]
for index, value in enumerate(colores):
    print(index, value)

    """
    tarea
    
    """

def print_numbers(Text1, Text2) -> int:
    count = 0 
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0 :
            print(Text1 + Text2)
        elif number % 3 == 0:
            print(Text1)
        elif number % 5 == 0:
            print(Text2)
        else :
            print(number)
            count += 1
    return count

print(print_numbers("Fizz","Buzz"))