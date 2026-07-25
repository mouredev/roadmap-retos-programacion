#FUNCIONES

#FUNCIONES DEFINIDAS POR EL USUARIO

#Simple
def greet():
    print("Hola, Python!")

greet()

#Con retorno
def return_greet():
    return "Hola, Python!"

print(return_greet())

#Con un argumento
def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Python")

#Con argumentos
def args_greet(name, greet):
    print(f"{greet}, {name}!")

args_greet("Python","Hola")
args_greet(greet="Hola",name="Python")

#Con un argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Python")
default_arg_greet()

#Con argumentos y retorno
def return_args_greet(name, greet):
    return(f"{greet}, {name}!")

print(return_args_greet("Python","Hola"))

#Con retorno de varios valores
def multiple_retur_greet():
    return "Hola", "Python"

greet, name = multiple_retur_greet()
print(f"{greet}, {name}!")

#Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Victor", "Todos")


#FUNCIONES DENTRO DE FUNCIONES

def outer_function():
    def inner_function():
        print("Hola, Python!")
    inner_function()

outer_function()


#FUNCIONES DEL LENGUAJE

print(len("Hola"))
print(type("Hola"))
print("Hola".upper())


#VARIABLES LOCALES Y GLOBALES

global_variable = "Python"

def hello_python():
    local_variable = "Hola"
    print(f"{local_variable}, {global_variable}!")


print(global_variable)
#print(local_variable)  No funciona al ser variable local de la funcion
hello_python()


#EJERCICIO EXTRA

def extra_function(cad1, cad2) -> int:
    cont = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{cad1} , {cad2}")
        elif i % 3 == 0:
            print(cad1)
        elif i % 5 == 0:
            print(cad2)
        else:
            print(i)
            cont += 1
    return cont

print(extra_function("M3","M5"))