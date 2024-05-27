# funciones simoples


def saludo():
    print ("hola python")


saludo()

# funcion con retorno

def return_saludo():
    return "hola, python"



print (return_saludo())


# funcion con argumento, argumentos, argumentos predeterminado

def return_argumento( nombre):
    print (f"hola, {nombre}")


return_argumento("simon")


def return_argumento(saludo, nombre):
    print (f"{saludo}, {nombre}")


return_argumento("hi", "simon")

def default_return_argumento(nombre="python"):
    print (f"hola,{nombre}!")


default_return_argumento("simon")
default_return_argumento()

# funcion con retorno de varios valores

def multiple_return_arguments():
    return "hola", "python"

saludo, nombre = multiple_return_arguments()
print(saludo)
print(nombre)

# funciones con numero variable de argumento

def variable_arg_saludo(*nombres):
    for nombre in nombres:
        print(f"hola, {nombre}")

variable_arg_saludo("python","simon","storbett")


# funcion con numero variable de argumento con palabra clave

def variable_key_arg_saludo(**nombres):
    for key, valor in nombres.items():
        print(f"{valor} ({key})")

variable_key_arg_saludo(
    lenguaje= "python",
    nombre = "simon",
    alias = "storbett",
    edad = 33
)

# funcion dentro de una funcion

def otra_funcion():
    def inner_funcion():
        print ("hola, python")
    inner_funcion()

otra_funcion()

# funciones dentro del lemguaje

print(len("storbett"))
print(type("storbett"))
print("storbett".upper())


# variables locales y globales

global_variable = "python"

print(global_variable)

def hello_python():
 local_variable = "hola"
 print(f"{local_variable}, {global_variable}")
    
hello_python()


# extra

def prueba (tex1, text2)-> int:
    count = 0
    for number in range(1, 101):
         if number % 3 == 0 and number % 5 == 0:
            print (tex1 + text2)
         elif number % 3 == 0:
            print(tex1)
         elif number % 5 == 0:
            print (text2)
         else: 
            print(number)
            count += 1
    return count

print(prueba("fizz","buzz"))